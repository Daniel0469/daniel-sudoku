"""main.py: Called when the package is run as a script."""

from .sudoku.sudoku_engine import Sudoku
from .logs.setup_logging import setup_logging

main_logger = setup_logging()


def main() -> None:
    """
    Main function for the application.

    Notes
    -----
    This function is the entry point for the application.
    """
    try:
        main_logger.info("Application started.")
        sudoku_game = Sudoku()
        sudoku_game.generate()
    except KeyboardInterrupt:
        print("\n")
        main_logger.info("Exiting application due to user interrupt...")


if __name__ == "__main__":
    main()