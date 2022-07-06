class InvalidOperationError(Exception):
    """Returns a message when the user tries to do a stack or queue operation on an empty stack or queue."""

    def __init__(self):
        self.message = "Method not allowed on empty collection"

    def __str__(self):
        return self.message
