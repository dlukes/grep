#!/usr/bin/env python3
"""Usage: grep.py PATTERN FILE

Print lines from FILE matching regular expression PATTERN.

"""

import sys
import re


def grep(pattern, lines):
    """Print lines matching pattern."""
    for line in lines:
        if re.search(pattern, line):
            print(line, end="")


def parse_argv(argv):
    """Parse script arguments."""
    pattern, path = argv
    return pattern, path


def main(argv):
    """Main entry point of script."""
    try:
        pattern, path = parse_argv(argv)
    except ValueError:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(1)
    try:
        with open(path) as file:
            grep(pattern, file)
    except FileNotFoundError as err:
        print(__doc__.strip(), file=sys.stderr)
        print(err, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
