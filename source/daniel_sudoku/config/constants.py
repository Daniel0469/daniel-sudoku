"""constants.py: Constants for the application."""


class Constants:
    """
    Constants for the application.

    Notes
    -----
    This class contains constants used throughout the application.
    By storing constants in a single location, it is easier to
    manage and update them. Constants should be defined as class
    attributes and should be named in uppercase with underscores
    separating words.
    """

    # Logging constants
    LOGGING_LEVEL_DEFAULT = "INFO"
    LOGGING_FORMAT = "%(message)s"
    LOGGING_DATE_FORMAT = "[%X]"
    LOGGING_TRACEBACKS = True
    
    # Sudoku constants
    BOARD_SIZE = (9, 9)