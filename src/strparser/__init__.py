"""
StrParser - Utilities for parsing and manipulating strings.
"""

from .substring import (
    substring_after,
    substring_after_last,
    substring_before,
    substring_between,
    substring_between_after_reference,
    substring_before_to,
    substring_by_index,
    SubstringNotFoundError,
    EmptyStringError,
    IndexOutOfRangeError,
)

__version__ = "0.1.2"
__author__ = "Javier Ojeda"
__all__ = [
    # Functions
    "substring_after",
    "substring_after_last",
    "substring_before",
    "substring_between",
    "substring_between_after_reference",
    "substring_before_to",
    "substring_by_index",
    # Exceptions
    "SubstringNotFoundError",
    "EmptyStringError",
    "IndexOutOfRangeError",
]