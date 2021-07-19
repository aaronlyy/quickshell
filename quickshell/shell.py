from shlex import split as _shsplit

from command import Command
from error import DuplicateCommandError, NotCallableError

class Shell:
    def __init__(self, name: str, prefix="[>]") -> None:
        self._name = name
        self._prefix = prefix
        self._commands = {}

    #*########################
    #*##     MAIN LOOP     ###
    #*########################
    def _loop(self):
        """Main loop for input and executing functions"""
        while True:
            inp = input(self._prefix)

            if inp:
                cmd, args = inp.split()[0], _shsplit(inp)[1:]
                if cmd in self._commands:
                    self._commands[cmd].execute(*args)
                else:
                    print("Command not found! Try 'help'.")

    #*########################
    #*## ADD NEW COMMANDS  ###
    #*########################
    def add_command(self, function, name: str = None) -> None:
        if callable(function):
            if not name:
                name = function.__name__
            if not name in self._commands:
                self._commands[name] = Command(function)
            else:
                raise DuplicateCommandError(name)
        else:
            raise NotCallableError(function)

    #*########################
    #*## INTERNAL COMMANDS ###
    #*########################
    def _add_internal_commands(self) -> None:
        self.add_command(self._cmd_exit, name="exit")
        self.add_command(self._cmd_about, name="about")
        self.add_command(self._cmd_help, name="help")

    def _cmd_exit(self) -> None:
        """
        Exit the shell
        """
        exit(0)

    def _cmd_about(self) -> None:
        """
        Show about text
        """
        print("""
        Made with ♥ by https://github.com/aaronlyy
        """)

    def _cmd_help(self):
        """
        Display help.
        """
        for k, v in self._commands.items():
            print(f"{k}: {v.desc()}")

    #*########################
    #*##        RUN        ###
    #*########################
    def run(self):
        self._add_internal_commands()
        self._loop()