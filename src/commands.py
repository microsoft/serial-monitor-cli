from serialMonitorCtrl import SerialMonitor
from abc import ABC


class Command(ABC):
    def __init__(self, serial: SerialMonitor):
        self._serial = serial

    def execute():
        pass


class rtsOn(Command):
    def execute(self):
        self._serial.setRts(True)


class rtsOff(Command):
    def execute(self):
        self._serial.setRts(False)


class dtrOn(Command):
    def execute(self):
        self._serial.setDtr(True)


class dtrOff(Command):
    def execute(self):
        self._serial.setDtr(False)


class close(Command):
    def execute(self):
        self._serial.close()


class write(Command):
    def execute(self):
        self._serial.write()


class CommandInvoker:
    def __init__(self, serial: SerialMonitor):
        self._ser = serial
        self._commands = {}
        self._next_command = None

    """
    Registers command object with a command name

    @param command_name: the name of the command as a string
    @param command: the corresponding command object
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
