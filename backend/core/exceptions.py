class TaskError(Exception):
    """Base class for exceptions in this module."""
    pass
class TaskNotFoundError(TaskError):
    """Raised when a task is not found."""
    pass
class TaskValidationError(TaskError):
    """Raised when task data is invalid."""
    pass