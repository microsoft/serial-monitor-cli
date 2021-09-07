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
        exit()


class write(Command):
    def __init__(self, serial: SerialMonitor):
        self._serial = serial

    def execute(self, dataToWrite):
        self._serial.write(dataToWrite)


class CommandInvoker:
    def __init__(self, serial: SerialMonitor):
        self._ser = serial
        self._commands = {}
        self._next_command = None

    """
    Registers command object with a command name

    @param command_name: the name of the command as a string
    @param command: the corrosponding command object
    """
    def registerCommand(self, command_name: str, command: Command):
        self._commands[command_name] = command

    """
    Sets the next command to be executed

    @param command: the name of the command to be set
    @raise KeyError: if command is invalid
    """
    def set_command(self, command: str) -> bool:
        try:
            self._commands[command]
        except KeyError:
            print("Invalid Command")
            return

        self._next_command = self._commands[command]

    """
    Excutes the next command and clear the queue
    """
    def executeCommand(self):
        self._next_command.execute()
        self._next_command = None

    """
    Process and execute external commands

    @param incoming_data: the data to be processed
    @raiseJSONDecodeError: if json format is invalid
    """
    def process_external_command(self, incoming_data: str):
        try:
            data_obj = json.loads(incoming_data)
            if data_obj['cmd']:
                self.set_command(data_obj['cmd'])
                if(self._next_command and data_obj['payload']):
                    self.executeCommand(data_obj['payload'])
                if(self._next_command):
                    self.executeCommand()

        except json.decoder.JSONDecodeError:
            print("Bad JSON format")
