"""paths.py: Contains paths for the application."""

import shutil
import tempfile
from importlib import resources
from pathlib import Path


class Paths:
    """
    Paths for the application.

    Notes
    -----
    This class contains paths used throughout the application.
    By storing paths in a single location, it is easier to manage and update them.
    Paths should be defined as class attributes and should be named in uppercase
    with underscores separating words.
    """

    temp_dir = Path(tempfile.mkdtemp())

    @classmethod
    def temporary_clone(cls, directory_to_clone: str) -> None:
        """
        Create a temporary clone of a directory.

        Parameters
        ----------
        cls : Paths
            The class instance.
        directory_to_clone : str
            The directory to clone.

        Notes
        -----
        This method creates a temporary clone of a directory.
        """
        package_to_clone = resources.files(directory_to_clone)

        shutil.rmtree(cls.temp_dir)
        cls.temp_dir.mkdir(parents=True, exist_ok=True)

        for file in package_to_clone.iterdir():
            if file.is_file():
                shutil.copy(str(file), str(cls.temp_dir))

    TEMPLATES_PATH = temp_dir


# Clone the templates directory to a temporary directory if rendering templates
# Paths.temporary_clone("daniel_sudoku.templates")