"""
StrParser - Utilidades para parsear y manipular strings.
"""

from .substring import (
    substring_after,
    substring_after_last,
    substring_before,
    substring_between,
    substring_between_after_reference,
    substring_before_to,
    substring_by_index,
)

__version__ = "0.1.1"
__author__ = "Javier Ojeda"
__all__ = [
    "substring_after",
    "substring_after_last",
    "substring_before",
    "substring_between",
    "substring_between_after_reference",
    "substring_before_to",
    "substring_by_index",
]