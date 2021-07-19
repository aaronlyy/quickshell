from inspect import getfullargspec as gfas
from inspect import ismethod

class Command:
    """
    Generic command class

    Args:
        function: "function"
    """
    def __init__(self, function: "function") -> None:
        if function.__doc__:
            description = function.__doc__
        else:
            description = "No description."
        if ismethod(function): # skip self argument
            arguments = [a for a in gfas(function).args if a != "self"]
        else:
            arguments = gfas(function).args
        self._cmd = {
                "function": function,
                "description": description,
                "arguments": arguments
        }

    def execute(self, *arguments) -> None:
        """
        Executes the function with given arguments
        """
        if len(arguments) == len(self._cmd["arguments"]): # needed and given args == 0
            self._cmd["function"](*arguments) # execute function with no arguments
        else:
            raise NotImplementedError

    def desc(self) -> str:
        """
        Returns the description string
        """
        return self._cmd["description"]

    def __repr__(self) -> str:
        return f"{self._cmd}"