#!/usr/bin/env python3

import sys
import re

pattern, path = sys.argv[1:]
with open(path) as file:
    for line in file:
        if re.search(pattern, line):
            # každý z řádků v prohledávaném souboru už na konci obsahuje znak
            # nového řádku, funkce print() by defaultně další přidala → to
            # nechceme, tak si pomocí argumentu end="" vyžádáme, aby funkce
            # print() další znak nového řádku už nepřidávala
            print(line, end="")
