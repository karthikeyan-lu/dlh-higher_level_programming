# Python Exceptions - AI Academy (DLH)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Level](https://img.shields.io/badge/Level-Intermediate-orange)

This project contains Python exercises for exception handling, safe output, defensive programming, error reporting, and raising exceptions.

---

## Objective

To write more robust Python programs by learning:

- Safe list and integer printing
- `try`, `except`, and `finally`
- Safe division patterns
- Element-wise list division
- Raising exceptions manually
- Writing errors to `stderr`
- Safely executing callback functions
- Translating bytecode-style logic

---

## Topics Covered

### Safe Printing

- Printing list elements safely
- Printing integers safely
- Printing only integer values from mixed lists

### Exception Flow

- `try`
- `except`
- `finally`
- Safe division
- Returning result counts

### Raising and Reporting Errors

- Raising `TypeError`
- Raising `NameError`
- Printing errors to `stderr`
- Safe function execution

---

## Requirements

- Python 3.x
- `pycodestyle`
- Function files should be importable by the provided main files
- Exceptions should be handled only where required by the task

---

## Files

| File | Description |
| --- | --- |
| `0-safe_print_list.py` | Safely prints a requested number of list elements |
| `1-safe_print_integer.py` | Safely prints an integer |
| `2-safe_print_list_integers.py` | Prints only integers from a list |
| `3-safe_print_division.py` | Divides two values and always prints the result |
| `4-list_division.py` | Divides two lists element by element |
| `5-raise_exception.py` | Raises a `TypeError` |
| `6-raise_exception_msg.py` | Raises a `NameError` with a message |
| `100-safe_print_integer_err.py` | Prints integer errors to `stderr` |
| `101-safe_function.py` | Executes a function safely |
| `102-magic_calculation.py` | Recreates logic from Python bytecode |

---

## Usage

Run a task with its main file:

```bash
python3 0-main.py
```

Import a function:

```python
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

safe_print_integer(89)
```

---

## Author

Karthikeyan Marimuthu - AI Academy, Digital Learning Hub Luxembourg
