#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieve position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not isinstance(value[0], int) or
            not isinstance(value[1], int) or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

        self.__position = value

    def area(self):
        """Return current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print square using # character."""
        if self.__size == 0:
            print()
            return

        # Print vertical spaces
        for _ in range(self.__position[1]):
            print()

        # Print square with horizontal spaces
        for _ in range(self.__size):
            print((" " * self.__position[0]) + ("#" * self.__size))

    def __str__(self):
        """Return printable square representation."""
        if self.__size == 0:
            return ""

        lines = []

        # Add vertical spacing
        for _ in range(self.__position[1]):
            lines.append("")

        # Add square lines
        for _ in range(self.__size):
            lines.append(
                (" " * self.__position[0]) + ("#" * self.__size)
            )

        return "\n".join(lines)
