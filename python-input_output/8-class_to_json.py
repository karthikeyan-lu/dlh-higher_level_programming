#!/usr/bin/python3
"""Module for converting class instances to dictionaries."""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization."""
    return obj.__dict__
