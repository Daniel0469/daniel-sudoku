"""sudoku_engine.py: Contains the sudoku game."""

from ..config.constants import Constants
from ..logs.setup_logging import setup_logging

sudoku_logger = setup_logging()


class Sudoku:
    """
    TODO: Write a docstring for the Sudoku class, using numpy style.
    """
    
    def __init__(self) -> None:
        """
        TODO: Write a docstring for the init constructor using numpy style.
        """
        self.board_size = Constants.BOARD_SIZE
        
    def generate(self) -> None:
        """
        TODO: Write a docstring for the generate method using numpy style.
        """
        pass