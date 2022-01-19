import json
from queue import Queue
from serialMonitorCtrl import SerialMonitor
from sys import stdin, stdout

"""
Read data written to console

@param queue: the queue to store the data in
"""


def read_from_console(queue) -> None:
    ''' Read data from console '''
    data = stdin.buffer.readline()
    queue.put(data)


"""
Process incoming json data and check for commands

@param incoming_data: data string that should be in json format
@param payload_queue: queue to store any payload that was sent with the command
"""


def process_incoming_data(incoming_data: str, payload_queue: Queue):
    try:
        data_obj = json.loads(incoming_data)
        if data_obj['cmd']:
            if('payload' in data_obj):
                payload_queue.put(data_obj['payload'])
            return data_obj['cmd']
    except json.decoder.JSONDecodeError:
        print("Bad JSON format")


"""
Write data to console

@param data: bytes or string to write to console
"""


def print_to_console(data: bytes or str):
    if type(data) is str:
        data = data.encode('utf-8')
    if data:
        stdout.buffer.write(data)
        stdout.buffer.flush()
    elif data is None:
        return


"""
Write data to console in json format

@param data: bytes or string to write to console
"""


def print_to_console_json(data: bytes or str):
    if type(data) is bytes:
        data = data.decode('utf-8')
    if data:
        output = {'payload': data}
        json_output = json.dumps(output)
        encoded_output = json_output.encode('utf-8')
        stdout.buffer.write(encoded_output)
        stdout.buffer.flush()
    elif data is None:
        return


"""
Read data from serial service

@param ser: the SerialMonitor object to read from
@param json: select whether to print data out as json to console
"""


def read_from_device(ser: SerialMonitor, json=False):
    while ser.isOpen():
        line = ser.read()
        if json:
            print_to_console_json(line)
        else:
            print_to_console(line)
