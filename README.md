# StrParser

# StrParser

[![PyPI version](https://badge.fury.io/py/strparser.svg)](https://badge.fury.io/py/strparser)
[![Python Version](https://img.shields.io/pypi/pyversions/strparser.svg)](https://pypi.org/project/strparser/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Simple utilities for extracting and manipulating text substrings in Python.


---

### 📦 Installation

```bash
pip install strparser
```

**Requirements:**  `Python 3.8+`

### 🚀 Quick Start

```python
from strparser import substring_after, substring_before, substring_between

# Extract text after a delimiter
substring_after("hello:world", ":")           # Returns: "world"

# Extract text before a delimiter
substring_before("hello:world", ":")          # Returns: "hello"

# Extract text between two delimiters
substring_between("[content]", "[", "]")      # Returns: "content"
```

### 📚 Available Functions

Substring Extraction

| Function | Description | Example |
|----------|-------------|---------|
| `substring_after(s, delim)` | Returns substring after the first occurrence of delimiter | `substring_after("a:b:c", ":")` → `"b:c"` |
| `substring_after_last(s, delim)` | Returns substring after the last occurrence of delimiter | `substring_after_last("a/b/c", "/")` → `"c"` |
| `substring_before(s, delim)` | Returns substring before the first occurrence of delimiter | `substring_before("a:b:c", ":")` → `"a"` |
| `substring_between(s, from, to)` | Returns substring between two delimiters | `substring_between("[x]", "[", "]")` → `"x"` |
| `substring_between_after_reference(s, ref, from, to)` | Returns substring between delimiters after a reference | See examples below |
| `substring_before_to(s, end, begin)` | Returns substring before end delimiter, after begin delimiter | `substring_before_to("a:b:c", "c", "a")` → `":b:"` |
| `substring_by_index(s, split_by, index)` | Returns element at specified index after splitting | `substring_by_index("a,b,c", ",", 1)` → `"b"` |


### 💡 Usage Examples
Basic Extraction

```python
from strparser import substring_after, substring_before, substring_between

text = "username:john_doe@email.com"

# Extract email domain
domain = substring_after(text, "@")                    # "email.com"

# Extract username
username = substring_between(text, ":", "@")           # "john_doe"
```

Working with Paths

```python
from strparser import substring_after_last, substring_before

path = "/home/user/documents/file.txt"

# Extract filename
filename = substring_after_last(path, "/")             # "file.txt"

# Extract extension
extension = substring_after_last(filename, ".")        # "txt"

# Extract filename without extension
name = substring_before(filename, ".")                 # "file"
```

Complex Parsing

```python
from strparser import substring_between_after_reference

log = "2024-01-15 INFO [Database] Connection established"

# Extract module name from log
module = substring_between_after_reference(log, "INFO ", "[", "]")  # "Database"
```

Safe Index Access

```python
from strparser import substring_by_index

csv_line = "John,Doe,30,Engineer"

# Get specific field
first_name = substring_by_index(csv_line, ",", 0)      # "John"
last_name = substring_by_index(csv_line, ",", 1)       # "Doe"
age = substring_by_index(csv_line, ",", 2)             # "30"

# Out of range returns empty string (no exception)
field = substring_by_index(csv_line, ",", 10)          # ""
```


### 🔧 Error Handling
All functions handle edge cases gracefully:

```python
from strparser import substring_after, substring_by_index

# Empty strings return empty string (not None)
substring_after("", ":")                               # ""
substring_after("hello", ":")                          # ""

# Invalid index raises ValueError
substring_by_index("a,b,c", ",", -1)                   # Raises ValueError

# Out of range index returns empty string
substring_by_index("a,b,c", ",", 10)                   # ""
```

### 📖 Documentation
Full documentation is available at: https://github.com/jojeda930307/strparser
#### Type Hints
All functions include type hints for better IDE support:
```python
def substring_after(s: str, delim: str) -> str:
    """Returns substring after the first occurrence of delimiter."""
```

### 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
1. Fork the repository
2. Create your feature branch `git checkout -b feature/amazing-feature`
3. Commit your changes `git commit -m 'Add some amazing feature'`
4. Push to the branch `git push origin feature/amazing-feature`
5. Open a Pull Request

### Running Tests

```bash
pip install pytest
pytest tests/ -v
```

### 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

### 🔗 Links

| Function | Description                               |
|----------|-------------------------------------------|
| PyPI     | https://pypi.org/project/strparser/       | 
| GitHub   | https://github.com/jojeda930307/strparser |
| Author   | Javier Ojeda                              |


### 📝 Changelog
- Version 0.1.1 (2026-03-07)
- Improved README with examples

### Version 0.1.0 (2026-03-07)
- Initial release
- Substring extraction functions
- Full type hinting support
- Comprehensive test suite



<div align="center">

Made with ❤️ by Javier Ojeda
Report a Bug · Request Feature
</div>