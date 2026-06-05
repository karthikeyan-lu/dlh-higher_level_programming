# Python Serialization - AI Academy (DLH)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![JSON](https://img.shields.io/badge/JSON-Serialization-green)
![CSV](https://img.shields.io/badge/CSV-Data-blue)
![XML](https://img.shields.io/badge/XML-Data-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project contains Python serialization exercises using JSON, Pickle, CSV, XML, and HTTP-based data transfer.

---

## Objective

To practice serialization and data exchange by learning:

- JSON serialization and deserialization
- Saving dictionaries to JSON files
- Loading JSON data from files
- Serializing custom objects with Pickle
- Deserializing Pickle objects safely
- Reading CSV files
- Converting CSV data to JSON
- Creating and parsing XML data
- Sending serialized data over HTTP

---

## Topics Covered

### JSON

- `json.dump()`
- `json.load()`
- Dictionary serialization
- JSON file persistence

### Pickle

- Custom object serialization
- Binary file handling
- Safe deserialization patterns

### CSV and XML

- `csv.DictReader`
- CSV to JSON conversion
- XML element creation
- XML parsing with `xml.etree.ElementTree`

### Network Serialization

- JSON payloads
- HTTP POST requests
- API-style data transfer

---

## Requirements

- Python 3.x
- JSON, Pickle, CSV, and XML standard libraries
- `requests` for network serialization tasks
- Input and output files provided in the project directory

---

## Files

| File | Description |
| --- | --- |
| `task_00_basic_serialization.py` | Serializes dictionaries to JSON and loads them back |
| `task_01_pickle.py` | Serializes and deserializes a custom object with Pickle |
| `task_02_csv.py` | Converts CSV data into JSON format |
| `task_03_xml.py` | Serializes dictionaries to XML and loads XML back |
| `task_04_net.py` | Sends serialized data over HTTP |
| `data.csv` | Sample CSV input |
| `data.json` | Sample JSON data |
| `data.xml` | Sample XML data |
| `object.pkl` | Pickle output artifact |

---

## Usage

Run a serialization task:

```bash
python3 0-main.py
```

Run the CSV conversion example:

```bash
python3 main_02_csv.py
```

---

## Author

Karthikeyan Marimuthu - AI Academy, Digital Learning Hub Luxembourg
