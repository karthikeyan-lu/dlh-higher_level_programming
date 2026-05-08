# Python Serialization – AI Academy (DLH)

This repository contains my exercises on Python Serialization as part of the AI Academy course at DLH. The project focuses on serialization and deserialization techniques using JSON, Pickle, CSV, and XML in Python.

## 📘 Objective

To strengthen Python serialization concepts by learning:

* JSON serialization and deserialization
* Saving Python dictionaries into JSON files
* Loading JSON data from files
* Serializing custom Python objects using Pickle
* Deserializing Pickle objects
* Reading CSV files
* Converting CSV data into JSON format
* XML serialization
* XML deserialization
* File handling in Python
* Exception handling during serialization

---

# 🧩 Topics Covered

## 📂 JSON Serialization

* Serializing Python dictionaries
* Deserializing JSON files
* Writing JSON files
* Reading JSON files
* Using `json.dump()`
* Using `json.load()`

---

## 🧱 Pickle Serialization

* Serializing custom Python objects
* Deserializing custom class instances
* Working with binary files
* Using `pickle.dump()`
* Using `pickle.load()`
* Exception handling for corrupted files

---

## 📊 CSV to JSON Conversion

* Reading CSV files
* Using `csv.DictReader`
* Converting CSV rows into dictionaries
* Serializing CSV data into JSON format
* Writing formatted JSON files

---

## 🌐 XML Serialization

* Creating XML elements
* Building XML trees
* Writing XML files
* Parsing XML files
* Reconstructing Python dictionaries from XML
* Using `xml.etree.ElementTree`

---

# ⚙️ Key Concepts Used

* file input/output
* JSON
* XML
* Pickle
* serialization
* deserialization
* dictionaries
* lists
* strings
* integers
* booleans
* custom classes
* binary files
* CSV
* exception handling
* `json.dump()`
* `json.load()`
* `pickle.dump()`
* `pickle.load()`
* `csv.DictReader`
* `ElementTree`
* loops
* conditionals
* `with` statement
* UTF-8 encoding

---

# 📁 Project Structure

```text
python-serialization/
│
├── task_00_basic_serialization.py
├── task_01_pickle.py
├── task_02_csv.py
├── task_03_xml.py
│
├── 0-main.py
├── 1-main.py
├── main_02_csv.py
├── main_03_xml.py
│
├── data.csv
├── data.json
├── data.xml
├── object.pkl
│
└── README.md
```

---

# 🚀 Tasks Overview

## 0. Basic Serialization

### File

`task_00_basic_serialization.py`

### Description

This task serializes a Python dictionary into a JSON file and deserializes the JSON file back into a Python dictionary.

### Functions

#### `serialize_and_save_to_file(data, filename)`

* Serializes a dictionary
* Saves data into a JSON file

#### `load_and_deserialize(filename)`

* Reads JSON data from a file
* Returns a Python dictionary

### Example Output

```python
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
```

---

## 1. Pickling Custom Classes

### File

`task_01_pickle.py`

### Description

This task demonstrates serialization and deserialization of custom Python objects using the `pickle` module.

### Class

#### `CustomObject`

### Attributes

* `name`
* `age`
* `is_student`

### Methods

#### `display()`

Displays object information.

#### `serialize(filename)`

* Serializes the object
* Saves it into a `.pkl` file

#### `deserialize(filename)`

* Loads serialized object data
* Returns a `CustomObject` instance

### Example Output

```text
Name: John
Age: 25
Is Student: True
```

---

## 2. Converting CSV Data to JSON Format

### File

`task_02_csv.py`

### Description

This task reads CSV data and converts it into JSON format.

### Function

#### `convert_csv_to_json(filename)`

* Reads CSV data
* Converts rows into dictionaries
* Writes JSON data into `data.json`
* Returns `True` if successful
* Returns `False` if an error occurs

### Example CSV Data

```csv
name,age,city
John,28,New York
Alice,24,Los Angeles
Bob,22,Chicago
Eve,30,San Francisco
```

### Example JSON Output

```json
[
    {
        "name": "John",
        "age": "28",
        "city": "New York"
    },
    {
        "name": "Alice",
        "age": "24",
        "city": "Los Angeles"
    }
]
```

---

## 3. Serializing and Deserializing with XML

### File

`task_03_xml.py`

### Description

This task demonstrates serialization and deserialization using XML format.

### Functions

#### `serialize_to_xml(dictionary, filename)`

* Serializes dictionary data into XML
* Saves XML data into a file

#### `deserialize_from_xml(filename)`

* Reads XML data
* Reconstructs Python dictionary

### Example XML Output

```xml
<data>
    <name>John</name>
    <age>28</age>
    <city>New York</city>
</data>
```

### Example Dictionary Output

```python
{'name': 'John', 'age': '28', 'city': 'New York'}
```

---

# 🎯 Learning Outcome

By completing this module, I am able to:

* Serialize Python dictionaries into JSON
* Deserialize JSON files into Python objects
* Save and load custom Python objects using Pickle
* Understand binary serialization
* Read and process CSV files
* Convert CSV data into JSON format
* Serialize data into XML format
* Deserialize XML data into Python dictionaries
* Handle exceptions during file operations
* Work with multiple serialization formats in Python
* Understand differences between JSON, Pickle, CSV, and XML
* Build reusable serialization functions
* Improve Python file handling skills

---

# 🛠️ Technologies Used

* Python 3
* JSON
* Pickle
* CSV
* XML
* ElementTree

---

# 👨‍💻 Author

Karthikeyan Marimuthu
