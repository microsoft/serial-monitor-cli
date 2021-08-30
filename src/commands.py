from serialMonitorCtrl import SerialMonitor
import json


class Command:
    def __init__(self, cmd, serial: SerialMonitor, setting=None):
        self._command = cmd
        self._serial = serial
        self._setting = setting

    def execute():
        pass


class rtsOn(Command):
    def execute(self):
        print("executed")
        self._serial.rts(True)
        pass


class rtsOff(Command):
    def execute():
        pass


class close(Command):
    def execute():
        pass


class CommandInvoker:
    # List of commands for input validation
    _commands = ['close',
                 'rtsOn',
                 'rtsOff',
                 'write']

    def __init__(self, serial: SerialMonitor):
        self._ser = serial

    def set_command(self, command: str) -> bool:
        try:
            self._commands.index(command)
        except ValueError:
            print("Invalid Command")
            return

        self._next_command = eval(command)

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
