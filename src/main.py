from serialMonitorCtrl import SerialMonitor
import argparse
import dataHandler as dataHandler
import threading
import queue
from commands import CommandInvoker

parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest='func')

ports_parser = subparser.add_parser('list-ports')

ser_parser = subparser.add_parser('open')
ser_parser.add_argument('port', type=str)
ser_parser.add_argument('-b', '--baud', type=int)
ser_parser.add_argument('-j', '--json', action='store_true')

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


if args.func == 'list-ports':
    dataHandler.print_to_console(SerialMonitor.get_port_list_json())
elif args.func == 'open':
    device_connection = SerialMonitor(args.port, args.baud)
    invoker = CommandInvoker(device_connection)
    device_connection.open()
    user_input_thread = create_user_input_thread(user_input_queue)
    device_connection_thread = create_device_connection_thread()
    try:
        user_input_thread.start()
        device_connection_thread.start()
        while True:

            if user_input_queue.empty() is False:
                user_input = user_input_queue.get()
                if args.json is True:
                    decoded_input = user_input.decode('utf-8').strip()
                    invoker.process_external_command(decoded_input)
                    # dataHandler.process_external_command(decoded_input,
                    #                                      device_connection)
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
