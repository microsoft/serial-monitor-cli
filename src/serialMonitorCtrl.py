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

    """
    Initialize and open new serial port
    """
    def open(self):
        try:
            self._serial = serial.Serial(self._port,
                                         self._baud,
                                         rtscts=self._rts,
                                         dsrdtr=self._rts)
        except SerialException:
            print(f'No device found at port {self._port}')
            raise SystemExit

    """
    Close the serial port
    """
    def close(self):
        self._serial.close()

    """
    Read line of data from serial connection

    @return: bytes of the data read
    @raise SerialException: if no device avialble at selected port
    """
    def read(self) -> bytes:
        if self.isOpen() is True:
            try:
                line = self._serial.readline()
                return line
            except SerialException:
                print(f'Connection lost to device at port {self._port}')
                raise SystemExit

    """
    Sends bytes to serial

    @param byteToSend: bytes to send to serial
    """
    def write(self, bytesToSend):
        self._serial.write(bytesToSend.encode('utf-8'))

    """
    Check if serial is open

    @return: true if port is open, otherwise false
    """
    def isOpen(self) -> bool:
        return(self._serial.isOpen())

    """
    Set the Ready to Send (rts) setting

    @param state: the desired state of the setting
    """
    def setRts(self, state: bool) -> None:
        self._serial.rts = state

    """
    Set the Data Terminal Ready (dtr) setting

    @param state: the desired state of the setting
    """
    def setDtr(self, state: bool) -> None:
        self._serial.dtr = state

    """
    Creates list of available serial ports and devices

    @return: list of dicts, one dict of each device (port, description, id)
    """
    @staticmethod
    def get_port_list() -> list:
        port_list = []
        for port, desc, hwid in sorted(comports()):
            port_list.append({'port': port, 'desc': desc, 'hwid': hwid})
            # port_list.update({port desc})
        return port_list

    """
    Convert port list to JSON

    @return: port list as a json object
    """
    @staticmethod
    def get_port_list_json() -> json:
        port_list_json_obj = json.dumps(SerialMonitor.get_port_list())
        return port_list_json_obj
