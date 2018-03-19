Jednoduchý klon programu `grep`
===============================

Repozitář zachycuje postupnou implementaci jednoduchého klonu standardního
unixového programu `grep` v Pythonu. Začíná od základní funkcionality a
postupně kód vylepšuje a učesává pomocí různých pokročilejších modulů, které
jsou při psaní programů pro příkazovou řádku dobrými pomocníky.

Jde zejména o tyto moduly:

- [fileinput](https://docs.python.org/3/library/fileinput.html)
- [logging](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)
- [argparse](https://docs.python.org/3/howto/argparse.html)

**Není pochopitelně nutné, aby s těmito moduly pracoval každý váš skript.**
Vyplatí se to zejména u těch, které mají víc různých způsobů využití, případně
jsou určeny i jiným lidem -- tam flexibilitu a pokročilejší funkce těchto
modulů oceníme. Ale u jednoúčelového skriptu, který budete využívat jen vy
sami, se s čistým svědomím můžete zastavit třeba [už v tomto
bodě](https://github.com/dlukes/grep/releases/tag/mvp-re), nemusíte ani řešit
ošetření chyb, stejně je nikdo jiný neuvidí.

Jak s repozitářem pracovat
--------------------------

### Ve zkratce

```console
user@host:~$ git clone https://github.com/dlukes/grep.git
user@host:~$ cd grep
user@host:~$ git log --reverse -p
```

### Detailněji

Komentáře v kódu a zprávy u *commitů* popisují, jak při implementaci krok za
krokem postupovat, vysvětlují motivaci jednotlivých kroků atp. Účelem je
**pročíst si historii repozitáře a seznámit se s moduly a postupy, které
implementaci programů pro příkazovou řádku usnadňují**. Finální verzi skriptu
`grep.py` pak můžete použít jako šablonu pro svoje vlastní skripty.

Kód si pochopitelně můžete prohlédnout přímo na GitHubu: v sekci
[*commits*](https://github.com/dlukes/grep/commits/master) si můžete rozkliknout
jednotlivé verze a zobrazit rozdíly (*diffy*) mezi nimi.

Volnější pole působnosti budete mít, když si repozitář lokálně naklonujete:

```console
user@host:~$ git clone https://github.com/dlukes/grep.git
user@host:~$ cd grep
```

Následně doporučuju zobrazit si přehled celé historie repozitáře:

```console
user@host:~/grep$ git log --oneline
2bb99e4 (HEAD -> master, origin/master, origin/HEAD) Přidat readme
df38f1a Automatické testy pomocí modulu doctest
7335537 Úprava funkce grep pro použití v jiných programech
e0c2c94 Zpracování parametrů pomocí modulu argparse
cea1f05 Zprávy uživateli pomocí modulu logging
33f2fc2 Prohledávání standardního vstupu
b81b040 Prohledat víc souborů najednou
0c8a180 Automatická úprava formátování
e1580cf Zamezit spuštění funkce main při importu
2aaf285 Obalit kód do funkcí
0df7a68 Ošetření chyb
1e886d5 (tag: mvp-re) Regulární výrazy
04d9c23 Minimum viable product
07b69d6 Předávání parametrů
74254f8 Shebang
7bb0db4 Hello, world!
```

Navigovat v ní posléze můžete díky identifikátorům *commitů* a příkazu `git
checkout`. Např. pokud chcete vrátit stav repozitáře na úplný začátek:

```console
user@host:~/grep$ git checkout 7bb0db4
# a takhle se zase vrátíte zpět na nejnovější commit
user@host:~/grep$ git checkout master
```

Pokud si chcete u vybraného *commitu* jen prohlédnout zprávu a *diff*, aniž
byste měnili stav repozitáře, použijte příkaz `git show`:

```console
user@host:~/grep$ git show 7bb0db4
```

Šikovný způsob, jak systematicky projít celou chronologii *commitů* (zprávy a
*diffy*), je pomocí příkazu `git log` (nejdřív se ujistěte, že stav repozitáře
je na nejnovějším commitu, tj. `git checkout master`):

```console
user@host:~/grep$ git log --reverse -p
```

License
-------

Copyright © 2018--present [ÚČNK][cnc]/David Lukeš

Distributed under the [GNU General Public License v3][gplv3]

[cnc]: http://korpus.cz
[gplv3]: http://www.gnu.org/licenses/gpl-3.0.en.html
