#!/usr/bin/env python3
"""
Module for converting CSV data into JSON format.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert CSV file data into JSON format and save to data.json.

    Args:
        filename (str): Name of the CSV input file.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        # Read CSV data
        with open(filename, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        # Write JSON data
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
