from serialMonitorCtrl import SerialMonitor
import json


class Command:
    def execute():
        pass


class rtsOn(Command):
    def __init__(self, serial: SerialMonitor):
        self._serial = serial

    def execute(self):
        self._serial.setRts(True)


class rtsOff(Command):
    def __init__(self, serial: SerialMonitor):
        self._serial = serial

    def execute(self):
        self._serial.setRts(False)


class dtrOn(Command):
    def __init__(self, serial: SerialMonitor):
        self._serial = serial

    def execute(self):
        self._serial.setDtr(True)


class dtrOff(Command):
    def __init__(self, serial: SerialMonitor):
        self._serial = serial

    def execute(self):
        self._serial.setDtr(False)


class close(Command):
    def __init__(self, serial: SerialMonitor):
        self._serial = serial

    def execute(self):
        self._serial.close()


class write(Command):
    def __init__(self, serial: SerialMonitor):
        self._serial = serial

    def execute(self):
        self._serial.write()


class CommandInvoker:
    def __init__(self, serial: SerialMonitor):
        self._ser = serial
        self._commands = {}

    def registerCommand(self, command_name: str, command: Command):
        self._commands[command_name] = command

    def set_command(self, command: str) -> bool:
        try:
            self._commands[command]
        except ValueError:
            print("Invalid Command")
            return

        self._next_command = self._commands[command]

    def executeCommand(self):
        self._next_command.execute()
        self._next_command = None

    def process_external_command(self, incoming_data: str):
        try:
            # add input validation
            # catch errors
            data_obj = json.loads(incoming_data)
            if data_obj['cmd']:
                self.set_command(data_obj['cmd'])
                if(self._next_command):
                    self.executeCommand()
            if data_obj['cmd'] == 'write':
                self._ser.write(data_obj['payload'])
            elif data_obj['cmd'] == 'close':
                self._ser.close()
                exit()
        except json.decoder.JSONDecodeError:
            print("Bad JSON format")
