"""0. Feladat: Számok kiírása
Írj egy programot, amely kiírja az 1-től 20-ig a számokat!
1
2
3
...
"""

for i in range(1, 21):
    print(i)

"""0.b Feladat: Számok kiírása
Írj egy programot, amely kiírja az 1-től 20-ig a számokat a minta alapján!
1 2 3 4 ...
"""
for i in range(1, 21):
    print(i, end=" ")

"""1. Feladat: Páros számok kiírása
Írj egy programot, amely kiírja az 1 és 20 közötti páros számokat!
2
4
6
..."""

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

"""2. Feladat: Számok összege
Készíts egy programot, amely kiszámítja és kiírja az 1 és 10 közötti számok összegét!
Az összeg: __
"""

osszeg = 0
for i in range(1, 10):
    osszeg += i
print("Az összeg:", osszeg)

"""2.b Feladat: Számok összege
Készíts egy programot, amely kiszámítja és kiírja az 1 és 100 közötti számok összegét!
Az összeg: __"""


osszeg = 0
for i in range(1, 101):
    osszeg += i
print("Az összeg:", osszeg)

"""3. Feladat: Szorzótábla
Készíts egy programot, amely kiírja a 7-es szorzótáblát 1-től 10-ig!
7 x 1 = 7
7 x 2 = 14"""

for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

"""4. Feladat: Számok visszafelé
Írj egy programot, amely kiírja a számokat 10-től 1-ig csökkenő sorrendben!
10
9
8"""

for i in range(10, 0, -1):
    print(i)

"""5. Feladat: Csillagok kirajzolása
Készíts egy programot, amely egy háromszöget rajzol csillagokból! Az első sorban 1 csillag, a másodikban 2, és így tovább, összesen 5 sorban.
*
**
***"""

for i in range(1, 6):
    print('*' * i)

"""6. Feladat: Számok négyzetei
Írj egy programot, amely kiírja az 1-től 10-ig terjedő számok négyzeteit!
1 négyzete: 1
2 négyzete: 4"""

for i in range(1, 11):
    print(f"{i} négyzete: {i ** 2}")

# """7. Feladat: Összeadás felhasználói bemenettel
# Készíts egy programot, amely megkérdezi a felhasználótól, hogy hány számot szeretne megadni, majd bekéri ezeket a számokat és összeadja őket!"""
#
# osszeg = 0
# darab = int(input("Hány számot szeretnél megadni? "))
#
# for i in range(darab):
#     szam = int(input("Adj meg egy számot: "))
#     osszeg += szam
#
# print("Az összeg:", osszeg)