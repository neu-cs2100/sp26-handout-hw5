"""
Stores data for a user's fingerprint, including the pixel data and metadata such as name and year.
"""
from typing import TypeVar
from __future__ import annotations

class Fingerprint:
    """Class to represent a fingerprint with associated metadata."""

    def __init__(
        self, data: list[list[str]], name: str, year: int, rows: int, cols: int
    ) -> None:
        """
        Initialize a Fingerprint object with the given data and metadata.

        Arguments:
            data (list[list[str]]): 2D list representing the fingerprint pixels
            name (str): Name associated with the fingerprint
            year (int): Year the fingerprint was recorded
            rows (int): Number of rows in the fingerprint data
            cols (int): Number of columns in the fingerprint data
        
        Raises:
            ValueError: If the data does not have the specified number of rows, or if
                    any row has more than the specified number of columns.
        """
        pass

    @classmethod
    def from_file(cls: type[Fingerprint], filename: str) -> Fingerprint:
        """
        Create a Fingerprint object by reading fingerprint data from the file.
        
        Args:
            filename (str): The path to the file containing the fingerprint data.
        
        Returns:
            Fingerprint: A new instance of the Fingerprint class initialized with 
                the data from the file
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        pass
