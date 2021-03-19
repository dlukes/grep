#!/usr/bin/env python3
"""Print lines from each FILE matching regular expression PATTERN.

"""

import sys
import fileinput as fi
import logging as log
import argparse
import re

log.basicConfig(level=log.INFO)


def grep(pattern, lines):
    """Yield lines matching pattern.

    >>> list(grep("a", ["cat", "dog", "mat", "cot"]))
    ['cat', 'mat']

    The pattern is interpreted as a regular expression:

    >>> list(grep("c.t", ["cat", "dog", "mat", "cot"]))
    ['cat', 'cot']

    """
    for line in lines:
        if re.search(pattern, line):
            yield line


def parse_argv(argv):
    """Parse script arguments."""
    parser = argparse.ArgumentParser(description=__doc__.strip())
    parser.add_argument("pattern", metavar="PATTERN", type=str, help="Pattern to match")
    parser.add_argument(
        "paths",
        metavar="FILE",
        type=str,
        nargs="+",
        help="Files to search (- for standard input)",
    )
    return parser.parse_args(argv)


def main(argv):
    """Main entry point of script."""
    args = parse_argv(argv)
    log.info(f"Searching for {args.pattern!r} in {args.paths!r}.")
    try:
        for matching_line in grep(args.pattern, fi.input(args.paths)):
            print(matching_line, end="")
    except FileNotFoundError as err:
        log.critical(err)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
