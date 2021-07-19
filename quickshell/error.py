class ShellError(Exception):
    pass

class DuplicateCommandError(ShellError):
    def __init__(self, name):
        self.message = f"'{name}': Command already exists."
    def __str__(self):
        return self.message

class NotCallableError(ShellError):
    def __init__(self, name):
        self.message = f"'{name}': Is not a callable function or method."
    def __str__(self):
        return self.message