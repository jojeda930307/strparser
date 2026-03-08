"""
Tests for the substring module.
Run with: pytest tests/ -v
"""

import pytest
from strparser import (
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


# =============================================================================
# LEGACY MODE TESTS (strict=False by default for backward compatibility)
# =============================================================================

class TestSubstringAfter:
    def test_basic(self):
        assert substring_after("hola:mundo", ":") == "mundo"

    def test_not_found(self):
        assert substring_after("hola", ":") == ""

    def test_empty_string(self):
        assert substring_after("", ":") == ""

    def test_empty_delim(self):
        assert substring_after("hola", "") == ""

    def test_multiple_occurrences(self):
        assert substring_after("a:b:c", ":") == "b:c"


class TestSubstringAfterLast:
    def test_basic(self):
        assert substring_after_last("a/b/c", "/") == "c"

    def test_not_found(self):
        assert substring_after_last("abc", "/") == ""

    def test_single_occurrence(self):
        assert substring_after_last("a/b", "/") == "b"


class TestSubstringBefore:
    def test_basic(self):
        assert substring_before("hola:mundo", ":") == "hola"

    def test_not_found(self):
        assert substring_before("mundo", ":") == ""

    def test_multiple_occurrences(self):
        assert substring_before("a:b:c", ":") == "a"


class TestSubstringBetween:
    def test_basic(self):
        assert substring_between("[contenido]", "[", "]") == "contenido"

    def test_not_found(self):
        assert substring_between("hola", "[", "]") == ""

    def test_empty_result(self):
        assert substring_between("[]", "[", "]") == ""


class TestSubstringBetweenAfterReference:
    def test_basic(self):
        texto = "ref:inicio[contenido]fin"
        assert substring_between_after_reference(texto, "ref:", "[", "]") == "contenido"

    def test_not_found(self):
        assert substring_between_after_reference("hola", "ref:", "[", "]") == ""


class TestSubstringBeforeTo:
    def test_basic(self):
        assert substring_before_to("a:b:c", "c", "a") == ":b:"

    def test_not_found(self):
        assert substring_before_to("abc", "z", "a") == ""


class TestSubstringByIndex:
    def test_basic(self):
        assert substring_by_index("a,b,c", ",", 1) == "b"

    def test_zero_index(self):
        assert substring_by_index("a,b,c", ",", 0) == "a"

    def test_out_of_range(self):
        assert substring_by_index("a,b,c", ",", 10) == ""

    def test_negative_index(self):
        with pytest.raises(ValueError):
            substring_by_index("a,b,c", ",", -1)

    def test_empty_string(self):
        assert substring_by_index("", ",", 0) == ""


class TestWithRealText:
    def test_historical_text(self):
        texto = """
        La trayectoria histórica del pueblo tlaxcalteca está marcada por dos acontecimientos
        fundamentales que definieron su destino.
        """

        assert "tlaxcalteca" in substring_after(texto, "pueblo")
        assert "La trayectoria histórica del" in substring_before(texto, "pueblo")
        assert "tlaxcalteca está marcada por" in substring_between(texto, "pueblo", "dos")


# =============================================================================
# STRICT MODE TESTS (strict=True)
# =============================================================================

class TestSubstringAfterStrict:
    def test_strict_mode_found(self):
        assert substring_after("hola:mundo", ":", strict=True) == "mundo"

    def test_strict_mode_not_found(self):
        with pytest.raises(SubstringNotFoundError):
            substring_after("hola", ":", strict=True)

    def test_strict_mode_empty_string(self):
        with pytest.raises(EmptyStringError):
            substring_after("", ":", strict=True)

    def test_strict_mode_empty_delim(self):
        with pytest.raises(EmptyStringError):
            substring_after("hola", "", strict=True)


class TestSubstringAfterLastStrict:
    def test_strict_mode_found(self):
        assert substring_after_last("a/b/c", "/", strict=True) == "c"

    def test_strict_mode_not_found(self):
        with pytest.raises(SubstringNotFoundError):
            substring_after_last("abc", "/", strict=True)

    def test_strict_mode_empty_string(self):
        with pytest.raises(EmptyStringError):
            substring_after_last("", "/", strict=True)


class TestSubstringBeforeStrict:
    def test_strict_mode_found(self):
        assert substring_before("hola:mundo", ":", strict=True) == "hola"

    def test_strict_mode_not_found(self):
        with pytest.raises(SubstringNotFoundError):
            substring_before("mundo", ":", strict=True)

    def test_strict_mode_empty_string(self):
        with pytest.raises(EmptyStringError):
            substring_before("", ":", strict=True)


class TestSubstringBetweenStrict:
    def test_strict_mode_found(self):
        assert substring_between("[contenido]", "[", "]", strict=True) == "contenido"

    def test_strict_mode_delim_from_not_found(self):
        with pytest.raises(SubstringNotFoundError):
            substring_between("contenido]", "[", "]", strict=True)

    def test_strict_mode_delim_to_not_found(self):
        with pytest.raises(SubstringNotFoundError):
            substring_between("[contenido", "[", "]", strict=True)

    def test_strict_mode_empty_string(self):
        with pytest.raises(EmptyStringError):
            substring_between("", "[", "]", strict=True)


class TestSubstringBetweenAfterReferenceStrict:
    def test_strict_mode_found(self):
        texto = "ref:inicio[contenido]fin"
        assert substring_between_after_reference(texto, "ref:", "[", "]", strict=True) == "contenido"

    def test_strict_mode_reference_not_found(self):
        with pytest.raises(SubstringNotFoundError):
            substring_between_after_reference("hola", "ref:", "[", "]", strict=True)

    def test_strict_mode_delim_not_found(self):
        with pytest.raises(SubstringNotFoundError):
            substring_between_after_reference("ref:inicio", "ref:", "[", "]", strict=True)


class TestSubstringBeforeToStrict:
    def test_strict_mode_found(self):
        assert substring_before_to("a:b:c", "c", "a", strict=True) == ":b:"

    def test_strict_mode_delim_end_not_found(self):
        with pytest.raises(SubstringNotFoundError):
            substring_before_to("abc", "z", "a", strict=True)

    def test_strict_mode_delim_begin_not_found(self):
        with pytest.raises(SubstringNotFoundError):
            substring_before_to("a:b:c", "c", "x", strict=True)


class TestSubstringByIndexStrict:
    def test_strict_mode_valid_index(self):
        assert substring_by_index("a,b,c", ",", 1, strict=True) == "b"

    def test_strict_mode_out_of_range(self):
        with pytest.raises(IndexOutOfRangeError):
            substring_by_index("a,b,c", ",", 10, strict=True)

    def test_strict_mode_negative_index(self):
        with pytest.raises(ValueError):
            substring_by_index("a,b,c", ",", -1, strict=True)

    def test_strict_mode_empty_string(self):
        with pytest.raises(EmptyStringError):
            substring_by_index("", ",", 0, strict=True)

    def test_strict_mode_empty_split_by(self):
        with pytest.raises(EmptyStringError):
            substring_by_index("a,b,c", "", 0, strict=True)


# =============================================================================
# BACKWARD COMPATIBILITY TESTS
# =============================================================================

class TestBackwardCompatibility:
    """
    Ensure default behavior (strict=False) matches v0.1.0.
    This is critical for users upgrading from v0.1.0 to v0.1.1.
    """

    def test_substring_after_default_no_exception(self):
        """Default should NOT raise exception (strict=False)"""
        assert substring_after("hola", ":") == ""

    def test_substring_before_default_no_exception(self):
        """Default should NOT raise exception (strict=False)"""
        assert substring_before("mundo", ":") == ""

    def test_substring_between_default_no_exception(self):
        """Default should NOT raise exception (strict=False)"""
        assert substring_between("hola", "[", "]") == ""

    def test_substring_by_index_default_no_exception(self):
        """Default should NOT raise exception (strict=False)"""
        assert substring_by_index("a,b,c", ",", 10) == ""

    def test_explicit_strict_false(self):
        """Explicit strict=False should work same as default"""
        assert substring_after("hola", ":", strict=False) == ""
        assert substring_before("mundo", ":", strict=False) == ""

    def test_negative_index_always_raises(self):
        """Negative index should ALWAYS raise ValueError (both modes)"""
        with pytest.raises(ValueError):
            substring_by_index("a,b,c", ",", -1)
        with pytest.raises(ValueError):
            substring_by_index("a,b,c", ",", -1, strict=True)


# =============================================================================
# EXCEPTION CLASSES TESTS
# =============================================================================

class TestExceptionClasses:
    """Test that custom exceptions are properly defined and importable."""

    def test_substring_not_found_error_is_value_error(self):
        """SubstringNotFoundError should be a subclass of ValueError"""
        assert issubclass(SubstringNotFoundError, ValueError)

    def test_empty_string_error_is_value_error(self):
        """EmptyStringError should be a subclass of ValueError"""
        assert issubclass(EmptyStringError, ValueError)

    def test_index_out_of_range_error_is_value_error(self):
        """IndexOutOfRangeError should be a subclass of ValueError"""
        assert issubclass(IndexOutOfRangeError, ValueError)

    def test_exceptions_have_message(self):
        """Exceptions should contain meaningful error messages"""
        with pytest.raises(SubstringNotFoundError) as exc_info:
            substring_after("hola", ":", strict=True)
        assert "':'" in str(exc_info.value) or "Delimiter" in str(exc_info.value)