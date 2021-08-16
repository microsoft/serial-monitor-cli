import json
from serialMonitorCtrl import SerialMonitor
from sys import stdin, stdout


def read_from_console(queue) -> None:
    ''' Read data from console '''
    data = stdin.buffer.readline()
    queue.put(data)


def print_to_console(data: bytes or str):
    if type(data) is str:
        data = data.encode('utf-8')
    if data:
        stdout.buffer.write(data)
        stdout.buffer.flush()
    elif data is None:
        return


def print_to_console_json(data: bytes or str):
    if type(data) is bytes:
        data = data.decode('utf-8').strip()
    if data:
        output = {'payload': data}
        json_output = json.dumps(output)
        encoded_output = json_output.encode('utf-8')
        stdout.buffer.write(encoded_output)
        stdout.buffer.flush()
    elif data is None:
        return


def process_external_command(incoming_data: str, ser: SerialMonitor):
    try:
        # add input validation
        # catch errors
        data_obj = json.loads(incoming_data)
        if data_obj['cmd'] == 'write':
            ser.write(data_obj['payload'])
        elif data_obj['cmd'] == 'close':
            ser.close()
            exit()
    except json.decoder.JSONDecodeError:
        print("Bad JSON format")


def read_from_device(ser: SerialMonitor, json=False):
    while ser.isOpen():
        line = ser.read()
        if json:
            print_to_console_json(line)
        else:
            print_to_console(line)
