#!/usr/bin/env python3
"""Usage: grep.py PATTERN FILE [FILE...]

Print lines from each FILE matching regular expression PATTERN. Pass `-` for
standard input.

"""

import sys
import fileinput as fi
import re


def grep(pattern, lines):
    """Print lines matching pattern."""
    for line in lines:
        if re.search(pattern, line):
            print(line, end="")


def parse_argv(argv):
    """Parse script arguments."""
    # pokud dostaneme míň než dva parametry, ručně vyvoláme ValueError
    if len(argv) < 2:
        raise ValueError
    # jinak bereme první parametr jako pattern a veškeré zbývající jako cesty k
    # souborům na prohledání
    pattern, paths = argv[0], argv[1:]
    return pattern, paths


def main(argv):
    """Main entry point of script."""
    try:
        pattern, paths = parse_argv(argv)
    except ValueError:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(1)
    try:
        grep(pattern, fi.input(paths))
    except FileNotFoundError as err:
        print(__doc__.strip(), file=sys.stderr)
        print(err, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
