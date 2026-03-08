"""
Utility module for extracting substrings from text.
"""


class SubstringNotFoundError(ValueError):
    """Raised when a delimiter is not found in strict mode."""
    pass


class EmptyStringError(ValueError):
    """Raised when an empty string is provided in strict mode."""
    pass


class IndexOutOfRangeError(ValueError):
    """Raised when an index is out of range in strict mode."""
    pass


def substring_after(s: str, delim: str, strict: bool = False) -> str:
    """
    Return the substring after the first occurrence of a delimiter.

    Args:
        s: The input string to process.
        delim: The delimiter to search for.
        strict: If True, raises exception when delimiter is not found.
                If False, returns empty string. (default: False)

    Returns:
        The substring after the delimiter, or an empty string if the delimiter
        is not found (when strict=False).

    Raises:
        SubstringNotFoundError: If strict=True and delimiter is not found.
        EmptyStringError: If strict=True and input string is empty.

    Examples:
        >>> substring_after("hola:mundo", ":")
        'mundo'
        >>> substring_after("hola", ":", strict=False)
        ''
        >>> substring_after("hola", ":", strict=True)
        SubstringNotFoundError: Delimiter ':' not found
    """
    if not s:
        if strict:
            raise EmptyStringError("Input string is empty")
        return ""

    if not delim:
        if strict:
            raise EmptyStringError("Delimiter is empty")
        return ""

    if delim not in s:
        if strict:
            raise SubstringNotFoundError(f"Delimiter '{delim}' not found in string")
        return ""

    return s.partition(delim)[2]


def substring_after_last(s: str, delim: str, strict: bool = False) -> str:
    """
    Return the substring after the last occurrence of a delimiter.

    Args:
        s: The input string to process.
        delim: The delimiter to search for.
        strict: If True, raises exception when delimiter is not found.
                If False, returns empty string. (default: False)

    Returns:
        The substring after the last delimiter, or an empty string if the
        delimiter is not found (when strict=False).

    Raises:
        SubstringNotFoundError: If strict=True and delimiter is not found.
        EmptyStringError: If strict=True and input string is empty.

    Examples:
        >>> substring_after_last("a/b/c", "/")
        'c'
        >>> substring_after_last("abc", "/", strict=False)
        ''
        >>> substring_after_last("abc", "/", strict=True)
        SubstringNotFoundError: Delimiter '/' not found in string
    """
    if not s:
        if strict:
            raise EmptyStringError("Input string is empty")
        return ""

    if not delim:
        if strict:
            raise EmptyStringError("Delimiter is empty")
        return ""

    if delim not in s:
        if strict:
            raise SubstringNotFoundError(f"Delimiter '{delim}' not found in string")
        return ""

    return s.rpartition(delim)[2]


def substring_before(s: str, delim: str, strict: bool = False) -> str:
    """
    Return the substring before the first occurrence of a delimiter.

    Args:
        s: The input string to process.
        delim: The delimiter to search for.
        strict: If True, raises exception when delimiter is not found.
                If False, returns empty string. (default: False)

    Returns:
        The substring before the delimiter, or an empty string if the
        delimiter is not found (when strict=False).

    Raises:
        SubstringNotFoundError: If strict=True and delimiter is not found.
        EmptyStringError: If strict=True and input string is empty.

    Examples:
        >>> substring_before("hola:mundo", ":")
        'hola'
        >>> substring_before("mundo", ":", strict=False)
        ''
        >>> substring_before("mundo", ":", strict=True)
        SubstringNotFoundError: Delimiter ':' not found in string
    """
    if not s:
        if strict:
            raise EmptyStringError("Input string is empty")
        return ""

    if not delim:
        if strict:
            raise EmptyStringError("Delimiter is empty")
        return ""

    if delim not in s:
        if strict:
            raise SubstringNotFoundError(f"Delimiter '{delim}' not found in string")
        return ""

    return s.partition(delim)[0]


def substring_between(s: str, delim_from: str, delim_to: str, strict: bool = False) -> str:
    """
    Return the substring between two delimiters.

    Args:
        s: The input string to process.
        delim_from: The starting delimiter.
        delim_to: The ending delimiter.
        strict: If True, raises exception when delimiters are not found.
                If False, returns empty string. (default: False)

    Returns:
        The substring between the delimiters, or an empty string if the
        delimiters are not found (when strict=False).

    Raises:
        SubstringNotFoundError: If strict=True and delimiters are not found.
        EmptyStringError: If strict=True and input string is empty.

    Examples:
        >>> substring_between("[contenido]", "[", "]")
        'contenido'
        >>> substring_between("hola", "[", "]", strict=False)
        ''
        >>> substring_between("hola", "[", "]", strict=True)
        SubstringNotFoundError: Delimiters not found in string
    """
    if not s:
        if strict:
            raise EmptyStringError("Input string is empty")
        return ""

    if not delim_from or not delim_to:
        if strict:
            raise EmptyStringError("One or both delimiters are empty")
        return ""

    # Find first delimiter
    if delim_from not in s:
        if strict:
            raise SubstringNotFoundError(f"Starting delimiter '{delim_from}' not found")
        return ""

    # Get substring after first delimiter
    after_first = s.partition(delim_from)[2]

    # Find second delimiter
    if delim_to not in after_first:
        if strict:
            raise SubstringNotFoundError(f"Ending delimiter '{delim_to}' not found")
        return ""

    return after_first.partition(delim_to)[0]


def substring_between_after_reference(
    s: str, reference: str, delim_from: str, delim_to: str, strict: bool = False
) -> str:
    """
    Return the substring between two delimiters after a reference substring.

    Args:
        s: The input string to process.
        reference: The reference substring where the search should begin.
        delim_from: The starting delimiter.
        delim_to: The ending delimiter.
        strict: If True, raises exception when delimiters are not found.
                If False, returns empty string. (default: False)

    Returns:
        The extracted substring, or an empty string if it cannot be found.

    Raises:
        SubstringNotFoundError: If strict=True and any delimiter/reference is not found.
        EmptyStringError: If strict=True and input string is empty.

    Examples:
        >>> substring_between_after_reference("a:b:c:d", "a:", "b:", ":d")
        'c'
        >>> substring_between_after_reference("hola", "ref:", "[", "]", strict=False)
        ''
    """
    if not s:
        if strict:
            raise EmptyStringError("Input string is empty")
        return ""

    if not reference:
        if strict:
            raise EmptyStringError("Reference string is empty")
        return ""

    if not delim_from or not delim_to:
        if strict:
            raise EmptyStringError("One or both delimiters are empty")
        return ""

    if reference not in s:
        if strict:
            raise SubstringNotFoundError(f"Reference '{reference}' not found")
        return ""

    # Get substring after reference
    after_ref = s.partition(reference)[2]

    # Use substring_between on the result
    return substring_between(after_ref, delim_from, delim_to, strict=strict)


def substring_before_to(s: str, delim_end: str, delim_begin: str, strict: bool = False) -> str:
    """
    Return the substring before an ending delimiter and after a starting delimiter.

    Args:
        s: The input string to process.
        delim_end: The ending delimiter.
        delim_begin: The starting delimiter.
        strict: If True, raises exception when delimiters are not found.
                If False, returns empty string. (default: False)

    Returns:
        The extracted substring, or an empty string if it cannot be found.

    Raises:
        SubstringNotFoundError: If strict=True and delimiters are not found.
        EmptyStringError: If strict=True and input string is empty.

    Examples:
        >>> substring_before_to("a:b:c", "c", "a")
        ':b:'
        >>> substring_before_to("abc", "z", "a", strict=False)
        ''
    """
    if not s:
        if strict:
            raise EmptyStringError("Input string is empty")
        return ""

    if not delim_end or not delim_begin:
        if strict:
            raise EmptyStringError("One or both delimiters are empty")
        return ""

    if delim_end not in s:
        if strict:
            raise SubstringNotFoundError(f"Ending delimiter '{delim_end}' not found")
        return ""

    # Get substring before end delimiter
    before_end = s.partition(delim_end)[0]

    if delim_begin not in before_end:
        if strict:
            raise SubstringNotFoundError(f"Starting delimiter '{delim_begin}' not found")
        return ""

    return before_end.partition(delim_begin)[2]


def substring_by_index(s: str, split_by: str, index: int = 0, strict: bool = False) -> str:
    """
    Return the element at a specific index after splitting the string.

    Args:
        s: The input string to process.
        split_by: The delimiter used to split the string.
        index: The index of the element to return (default: 0).
        strict: If True, raises exception when index is out of range.
                If False, returns empty string. (default: False)

    Returns:
        The element at the specified index, or an empty string if the index
        does not exist (when strict=False).

    Raises:
        ValueError: If the index is negative.
        IndexOutOfRangeError: If strict=True and index is out of range.
        EmptyStringError: If strict=True and input string is empty.

    Examples:
        >>> substring_by_index("a,b,c", ",", 1)
        'b'
        >>> substring_by_index("a,b,c", ",", 10, strict=False)
        ''
        >>> substring_by_index("a,b,c", ",", 10, strict=True)
        IndexOutOfRangeError: Index 10 out of range
    """
    if not s:
        if strict:
            raise EmptyStringError("Input string is empty")
        return ""

    if not split_by:
        if strict:
            raise EmptyStringError("Split delimiter is empty")
        return ""

    if index < 0:
        raise ValueError("Index cannot be negative")

    splitted = s.split(split_by)

    if index >= len(splitted):
        if strict:
            raise IndexOutOfRangeError(f"Index {index} out of range (max: {len(splitted) - 1})")
        return ""

    return splitted[index]