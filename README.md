# FXReplay Bot

# A bot használata

### Ezt a szkriptet akkor is használhatod, ha nincs telepített python környezeted .

### Futtatás

**Python telepítve**

Először telepítse a szkripthez szükséges könyvtárakat a következő paranccsal

`pip install -r requirements.txt`

Ezután futtassa a main.py fájlt

`python main.py`

Ez a kódot headless módban futtatja, így a felhasználó nem látja a szkriptet a böngészőben dolgozni, csak az output lesz látható.

**Python nem telepítve**

A dist mappában kattintson duplán a main.exe programra, vagy futtassa a következőképpen

`start ./main.exe`
or
`start ./dist/main.exe`

attól függően, hogy honnan futtatjuk le a parancsot


## Használat

A futtatást követően az alábbi menüt kapjuk

![Fő menü](https://cdn.discordapp.com/attachments/1134077926808244318/1211287387829968916/image.png?ex=65eda649&is=65db3149&hm=69f6d494fd011a68c085cd2ef5bd0e0af5859175fc371a2d86a85c3ede1d5073&)

**Itt 4 opciónk van**

1. Egy tempmail szolgáltatónál automatikusan létrehozz egy e-mail címet a program, amit felhasznál, majd a regisztrációs fázisnál és magától verifikálja is a fiókot
2. Egy tetszőleges e-mailt adhatunk meg a programnak ahová kapjuk, majd a verifikációhoz szükséges linket itt viszont **magunknak kell, majd a megerősítő linkre nyomni**
3. A lokálisan lementett fiókokat és azok adatait írja ki a program egy táblázatban

