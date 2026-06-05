# Python Input/Output - AI Academy (DLH)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![JSON](https://img.shields.io/badge/JSON-Serialization-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Level](https://img.shields.io/badge/Level-Intermediate-orange)

This project contains Python exercises for file handling, JSON serialization, object serialization, dynamic object reloading, and Pascal's Triangle.

---

## Objective

To strengthen Python input/output skills by learning:

- Reading text files
- Writing and appending text files
- Working with UTF-8 encoding
- Converting objects to JSON strings
- Loading JSON strings into Python objects
- Saving and loading JSON files
- Converting class instances into dictionaries
- Filtering object attributes
- Reloading object data from dictionaries
- Generating Pascal's Triangle

---

## Topics Covered

### File Handling

- Reading files
- Writing files
- Appending text
- Using `with`
- Managing file paths safely

### JSON Serialization

- `json.dumps()`
- `json.loads()`
- `json.dump()`
- `json.load()`
- Saving Python objects to files
- Loading Python objects from files

### Object Serialization

- `__dict__`
- Attribute filtering
- `setattr()`
- Object reload methods
- Student class serialization

### Algorithms

- Pascal's Triangle
- Nested list construction

---

## Requirements

- Python 3.x
- `pycodestyle`
- UTF-8 file handling
- Modules, classes, and functions should be documented where required

---

## Files

| File | Description |
| --- | --- |
| `0-read_file.py` | Reads and prints a text file |
| `1-write_file.py` | Writes text to a file and returns character count |
| `2-append_write.py` | Appends text to a file and returns character count |
| `3-to_json_string.py` | Converts an object to a JSON string |
| `4-from_json_string.py` | Converts a JSON string to a Python object |
| `5-save_to_json_file.py` | Saves an object to a JSON file |
| `6-load_from_json_file.py` | Loads an object from a JSON file |
| `7-add_item.py` | Adds command-line arguments to a JSON list file |
| `8-class_to_json.py` | Returns a dictionary description of an object |
| `9-student.py` | Defines a basic `Student` class with JSON export |
| `10-student.py` | Adds filtered attribute export to `Student` |
| `11-student.py` | Adds JSON reload support to `Student` |
| `12-pascal_triangle.py` | Generates Pascal's Triangle |
| `100-append_after.py` | Inserts text after lines containing a search string |
| `101-generator.py` | Streams and aggregates user data with generators |
| `101-stats.py` | Reads stdin logs and computes metrics |

---

## Usage

Run a task with its main file:

```bash
python3 0-main.py
```

Run the JSON argument task:

```bash
python3 7-add_item.py Best School
```

---

## Author

Karthikeyan Marimuthu - AI Academy, Digital Learning Hub Luxembourg
