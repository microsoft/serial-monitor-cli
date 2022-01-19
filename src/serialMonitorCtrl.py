import serial
from serial.serialutil import SerialException
from serial.tools.list_ports import comports
import json


line_endings = {'nl': '\n',
                'cr': '\r',
                'crnl': '\r\n',
                'none': None}


class SerialMonitor:

    def __init__(self,
                 port,
                 baud,
                 input_payload_queue,
                 eol,
                 rts=False,
                 dtr=True):
        self._port = port
        self._baud = baud
        self._rts = rts
        self._dtr = dtr
        self._input_payload_queue = input_payload_queue
        self._commands = None
        self._endOfLine = line_endings[eol]

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
    Close the serial port and exit program
    """
    def close(self):
        self._serial.close()
        exit()

    """
    Read line of data from serial connection

    @return: bytes of the data read
    @raise SerialException: if no device available at selected port
    """
    def read(self) -> bytes:
        if self.isOpen() is True:
            try:
                return self._serial.read_all()
            except (SerialException, TypeError, AttributeError):
                print(f'Connection closed to device at port {self._port}')
                raise SystemExit

    """
    Sends bytes to serial
    """
    def write(self):
        bytesToSend = self._input_payload_queue.get() + self._endOfLine
        self._serial.write(bytesToSend.encode('utf-8'))
        self._serial.flush()

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
        return port_list

    """
    Convert port list to JSON

    @return: port list as a json object
    """
    @staticmethod
    def get_port_list_json() -> json:
        port_list_json_obj = json.dumps(SerialMonitor.get_port_list())
        return port_list_json_obj
