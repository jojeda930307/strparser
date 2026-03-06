"""
Tests para el módulo substring.
Ejecutar con: pytest tests/ -v
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
)


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