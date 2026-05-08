#!/usr/bin/env python3
"""
Module for XML serialization and deserialization.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary into XML format and save to a file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): Output XML filename.
    """
    # Create root element
    root = ET.Element("data")

    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create XML tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a dictionary.

    Args:
        filename (str): XML filename.

    Returns:
        dict: Deserialized dictionary.
    """
    # Parse XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Reconstruct dictionary
    data = {}

    for child in root:
        data[child.tag] = child.text

    return data
