"""
Utility module for extracting substrings from text.
"""


def substring_after(s: str, delim: str) -> str:
    """
    Return the substring after the first occurrence of a delimiter.

    Args:
        s: The input string to process.
        delim: The delimiter to search for.

    Returns:
        The substring after the delimiter, or an empty string if the delimiter
        is not found.

    Examples:
        >>> substring_after("hola:mundo", ":")
        'mundo'
        >>> substring_after("hola", ":")
        ''
    """
    if not s or not delim:
        return ""
    return s.partition(delim)[2] if delim in s else ""


def substring_after_last(s: str, delim: str) -> str:
    """
    Return the substring after the last occurrence of a delimiter.

    Args:
        s: The input string to process.
        delim: The delimiter to search for.

    Returns:
        The substring after the last delimiter, or an empty string if the
        delimiter is not found.

    Examples:
        >>> substring_after_last("a/b/c", "/")
        'c'
        >>> substring_after_last("a/b", "/")
        'b'
    """
    if not s or not delim:
        return ""
    return s.rpartition(delim)[2] if delim in s else ""


def substring_before(s: str, delim: str) -> str:
    """
    Return the substring before the first occurrence of a delimiter.

    Args:
        s: The input string to process.
        delim: The delimiter to search for.

    Returns:
        The substring before the delimiter, or an empty string if the
        delimiter is not found.

    Examples:
        >>> substring_before("hola:mundo", ":")
        'hola'
        >>> substring_before("mundo", ":")
        ''
    """
    if not s or not delim:
        return ""
    return s.partition(delim)[0] if delim in s else ""


def substring_between(s: str, delim_from: str, delim_to: str) -> str:
    """
    Return the substring between two delimiters.

    Args:
        s: The input string to process.
        delim_from: The starting delimiter.
        delim_to: The ending delimiter.

    Returns:
        The substring between the delimiters, or an empty string if the
        delimiters are not found.

    Examples:
        >>> substring_between("[contenido]", "[", "]")
        'contenido'
        >>> substring_between("hola", "[", "]")
        ''
    """
    if not s or not delim_from or not delim_to:
        return ""
    return substring_before(substring_after(s, delim_from), delim_to) if delim_from and delim_to in s else ""


def substring_between_after_reference(
        s: str, reference: str, delim_from: str, delim_to: str
) -> str:
    """
    Return the substring between two delimiters after a reference substring.

    Args:
        s: The input string to process.
        reference: The reference substring where the search should begin.
        delim_from: The starting delimiter.
        delim_to: The ending delimiter.

    Returns:
        The extracted substring, or an empty string if it cannot be found.

    Examples:
        >>> substring_between_after_reference("a:b:c:d", "a:", "b:", ":d")
        'c'
    """
    if not s or not reference or not delim_from or not delim_to:
        return ""
    return substring_between(substring_after(s, reference), delim_from, delim_to) if delim_from and delim_to and reference in s else ""


def substring_before_to(s: str, delim_end: str, delim_begin: str) -> str:
    """
    Return the substring before an ending delimiter and after a starting delimiter.

    Args:
        s: The input string to process.
        delim_end: The ending delimiter.
        delim_begin: The starting delimiter.

    Returns:
        The extracted substring, or an empty string if it cannot be found.

    Examples:
        >>> substring_before_to("a:b:c", "c", "a")
        ':b:'
    """
    if not s or not delim_end or not delim_begin:
        return ""
    return substring_after_last(substring_before(s, delim_end), delim_begin) if delim_end and delim_begin in s else ""


def substring_by_index(s: str, split_by: str, index: int = 0) -> str:
    """
    Return the element at a specific index after splitting the string.

    Args:
        s: The input string to process.
        split_by: The delimiter used to split the string.
        index: The index of the element to return (default: 0).

    Returns:
        The element at the specified index, or an empty string if the index
        does not exist.

    Raises:
        ValueError: If the index is negative.

    Examples:
        >>> substring_by_index("a,b,c", ",", 1)
        'b'
        >>> substring_by_index("a,b,c", ",", 10)
        ''
    """
    if not s or not split_by:
        return ""
    if index < 0:
        raise ValueError("Index cannot be negative")

    splitted = s.split(split_by)
    return splitted[index] if index < len(splitted) and split_by in s else ""