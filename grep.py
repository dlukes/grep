#!/usr/bin/env python3

# následující textový řetězec obsahuje úvodní informace ke skriptu jako celku.
# je dostupný přes speciální proměnnou `__doc__`, čehož využijeme níže.
"""Usage: grep.py PATTERN FILE

Print lines from FILE matching regular expression PATTERN.

"""

import sys
import re

# jak jsme zjistili, v tomto bodě může nastat ValueError (viz předchozí commit
# message). měli bychom ji tedy odchytit a pokud nastane, zobrazit uživateli
# nějakou užitečnější zprávu -- třeba návod, jak program používat správně,
# obsažený v proměnné __doc__, protože ta ValueError je prapůvodně způsobená
# tím, že uživatel programu předal špatný počet parametrů.
try:
    pattern, path = sys.argv[1:]
except ValueError:
    # abychom nemíchali užitečný výstup programu -- profiltrované řádky ze
    # souboru -- s chybovými hláškami, tiskneme chybové hlášky na tzv. chybový
    # výstup (standard error → sys.stderr). užitečný výstup jde naopak na tzv.
    # standardní výstup (standard output → sys.stdout), který u funkce print()
    # není potřeba specifikovat, protože je to default. v terminálu se sice
    # vytiskne obojí zároveň, ale např. k dalšímu zpracování skrz roury se
    # posílá jen standardní výstup.
    print(__doc__.strip(), file=sys.stderr)
    # funkce sys.exit() okamžitě ukončí program; konvence je, že jakékoli jiné
    # číslo než 0 (standardně se používá 1) naznačí, že běh programu neskončil
    # úspěchem
    sys.exit(1)

# při otevírání souboru může zase nastat FileNotFoundError (jak jsme také
# zjistili při testování předchozí verze skriptu). vypořádáme se s ní podobně:
try:
    with open(path) as file:
        for line in file:
            if re.search(pattern, line):
                print(line, end="")
# navíc si ale uložíme samotnou chybu do proměnné err a vytiskneme ji taky,
# abychom uživateli dali bližší nápovědu, v čem je problém
except FileNotFoundError as err:
    print(__doc__.strip(), file=sys.stderr)
    print(err, file=sys.stderr)
    sys.exit(1)
