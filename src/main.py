from serialMonitorCtrl import SerialMonitor
import argparse
import dataHandler as dataHandler
import threading
import queue
from commands import close, CommandInvoker, dtrOff, dtrOn, rtsOff, rtsOn, write
from time import sleep

parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest='func')

ports_parser = subparser.add_parser('list-ports',
                                    help='List all available serial ports')

ser_parser = subparser.add_parser('open',
                                  help='Open a new serial connection')
ser_parser.add_argument('port', type=str,
                        help='The port name to open. '
                        'Hint: Use list-ports to see available ports')
ser_parser.add_argument('-b', '--baud', type=int, metavar='9600',
                        help='The baud rate for the connection')
ser_parser.add_argument('-r', '--rtscts', action='store_true',
                        help='Set RTS/CTS to true')
ser_parser.add_argument('-d', '--dsrdtr', action='store_true',
                        help='Set DSR/DTR to true')
ser_parser.add_argument('-e',
                        '--eol',
                        choices=["nl", "cr", "crnl", 'none'],
                        const='nl',
                        nargs='?',
                        default='nl',
                        help='Line ending character on out going message\
                            choose from newline [nl], carriage return [cr],\
                            both [crnl], or none [none]')
ser_parser.add_argument('-j', '--json', action='store_true',
                        help='Set input and output to json mode')
ser_parser.add_argument('-t', '--timestamp', type=str,
                        metavar='"%H:%M:%S.%f -> "', default='',
                        help='Format of timestamp added before each line.\
                        List of all possible formats: https://strftime.org')

args = parser.parse_args()


def create_user_input_thread(queue: queue.Queue) -> threading.Thread:
    thread = threading.Thread(target=dataHandler.read_from_console,
                              args=[queue],
                              name="user_input",
                              daemon=True)
    return thread


def create_device_connection_thread() -> threading.Thread:
    thread = threading.Thread(target=dataHandler.read_from_device,
                              args=[device_connection, args.json],
                              name="device_connection",
                              daemon=True)
    return thread


user_input_queue = queue.Queue()
input_payload_queue = queue.Queue()


if args.func == 'list-ports':
    dataHandler.print_to_console(SerialMonitor.get_port_list_json())
elif args.func == 'open':
    device_connection = SerialMonitor(args.port,
                                      args.baud,
                                      input_payload_queue,
                                      args.eol,
                                      args.rtscts,
                                      args.dsrdtr,
                                      args.timestamp)
    invoker = CommandInvoker(device_connection)
    invoker.registerCommand('rtsOn', rtsOn(device_connection))
    invoker.registerCommand('rtsOff', rtsOff(device_connection))
    invoker.registerCommand('dtrOn', dtrOn(device_connection))
    invoker.registerCommand('dtrOff', dtrOff(device_connection))
    invoker.registerCommand('close', close(device_connection))
    invoker.registerCommand('write', write(device_connection))
    device_connection.open()
    user_input_thread = create_user_input_thread(user_input_queue)
    device_connection_thread = create_device_connection_thread()
    try:
        user_input_thread.start()
        device_connection_thread.start()
        while True:
            sleep(0.001)
            if user_input_queue.empty() is False:
                user_input = user_input_queue.get()
                if args.json is True:
                    decoded_input = user_input.decode('utf-8').strip()
                    command = dataHandler.process_incoming_data(decoded_input,
                                                                input_payload_queue)  # noqa: E501
                    if (command):
                        invoker.set_command(command)
                        invoker.executeCommand()

                else:
                    dataHandler.print_to_console(user_input)

            if user_input_thread.is_alive() is False:
                user_input_thread = create_user_input_thread(user_input_queue)
                user_input_thread.start()

            if device_connection_thread.is_alive():
                continue
            else:
                raise SystemExit

    except KeyboardInterrupt:
        device_connection.close()
        raise SystemExit
