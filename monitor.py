import serial
from serial.tools.list_ports import comports
import json


class SerialMonitor:

    def __init__(self, port, baud):
        self._port = port
        self._baud = baud

    def open(self):
        self._serial = serial.Serial(self._port, self._baud)

    def read(self):
        line = self._serial.readline()
        return line
        # with self._serial as serial:
        #     line = serial.readline()
        #     return line

    @staticmethod
    def get_port_list() -> list:
        # for port, desc, hwid in sorted(comports()):
        #     print("{}: {} [{}]".format(port, desc, hwid))
        list = comports()
        return list[0].device

    @staticmethod
    def get_port_list_json():
        port_list_json_obj = json.dumps(SerialMonitor.get_port_list())
        return port_list_json_obj


def main():
    print(SerialMonitor.get_port_list_json())


if __name__ == "__main__":
    main()
