#!/usr/bin/python3
"""Log parsing script."""

import sys


def print_stats(total_size, status_counts):
    """Print accumulated metrics."""
    print("File size: {}".format(total_size))

    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    line_count = 0
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_counts = {code: 0 for code in valid_codes}

    try:
        for line in sys.stdin:
            parts = line.split()

            if len(parts) >= 2:
                status_code = parts[-2]
                file_size = parts[-1]

                try:
                    total_size += int(file_size)
                except ValueError:
                    pass

                if status_code in status_counts:
                    status_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

        print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise
