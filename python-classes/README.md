# Python Classes and Objects - AI Academy (DLH)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OOP](https://img.shields.io/badge/OOP-Classes%20and%20Objects-purple)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Level](https://img.shields.io/badge/Level-Intermediate-orange)

This project contains Python object-oriented programming exercises using classes, private attributes, properties, validation, custom printing, linked lists, and operator overloading.

---

## Objective

To strengthen object-oriented programming skills by learning:

- Creating classes and objects
- Using constructors
- Managing private attributes
- Validating attributes
- Using getters, setters, and `@property`
- Creating instance methods
- Printing custom object output
- Implementing linked data structures
- Overloading comparison operators

---

## Topics Covered

### Classes and Encapsulation

- Empty classes
- Private attributes
- Name mangling
- Constructor initialization
- Attribute validation

### Properties and Methods

- Getter methods
- Setter methods
- Area calculation
- Square printing
- Position handling
- String representation

### Advanced OOP

- Singly linked lists
- Sorted insertion
- Magic methods
- Object comparison by area

---

## Requirements

- Python 3.x
- `pycodestyle`
- Modules, classes, and methods should be documented where required
- Class attributes should be validated according to task requirements

---

## Files

| File | Description |
| --- | --- |
| `0-square.py` | Defines an empty `Square` class |
| `1-square.py` | Adds a private size attribute |
| `2-square.py` | Adds size validation |
| `3-square.py` | Adds area calculation |
| `4-square.py` | Adds property getter and setter methods |
| `5-square.py` | Adds square printing with `#` |
| `6-square.py` | Adds position support and string representation |
| `100-singly_linked_list.py` | Implements a sorted singly linked list |
| `101-square.py` | Adds advanced position-based square printing |
| `102-square.py` | Adds square comparison operators |

---

## Usage

Run a task with its main file:

```bash
python3 6-main.py
```

Import a class:

```python
Square = __import__('3-square').Square

square = Square(5)
print(square.area())
```

---

## Author

Karthikeyan Marimuthu - AI Academy, Digital Learning Hub Luxembourg
