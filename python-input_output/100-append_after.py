#!/usr/bin/python3
"""Module for inserting text after matching lines."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing search_string."""

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    updated_lines = []

    for line in lines:
        updated_lines.append(line)

        if search_string in line:
            updated_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(updated_lines)
