import serial
from serial.serialutil import SerialException
from serial.tools.list_ports import comports
import json


class SerialMonitor:

    def __init__(self, port, baud, rts=False, dtr=True):
        self._port = port
        self._baud = baud
        self._rts = rts
        self._dtr = dtr
        self._commands = None

    def open(self):
        """Open serial port"""
        try:
            self._serial = serial.Serial(self._port,
                                         self._baud,
                                         rtscts=self._rts,
                                         dsrdtr=self._rts)
        except SerialException:
            print(f'No device found at port {self._port}')
            raise SystemExit

    def close(self):
        """Close serial port"""
        self._serial.close()

    def read(self) -> bytes:
        """Return line from serial"""
        if self.isOpen() is True:
            try:
                line = self._serial.readline()
                return line
            except SerialException:
                print(f'Connection lost to device at port {self._port}')
                raise SystemExit

    def write(self, bytesToSend):
        """Sends bytes to serial"""
        self._serial.write(bytesToSend.encode('utf-8'))

    def isOpen(self) -> bool:
        return(self._serial.isOpen())

    def setRts(self, state: bool) -> None:
        self._serial.rts = state

    def setDtr(self, state: bool) -> None:
        self._serial.dtr = state

    @staticmethod
    def get_port_list() -> list:
        """Return list of available serial ports and devices."""
        port_list = []
        for port, desc, hwid in sorted(comports()):
            port_list.append({'port': port, 'desc': desc, 'hwid': hwid})
            # port_list.update({port desc})
        return port_list

    @staticmethod
    def get_port_list_json():
        """Return list of available serial ports as JSON"""
        port_list_json_obj = json.dumps(SerialMonitor.get_port_list())
        return port_list_json_obj
