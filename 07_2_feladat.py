"""
2. Feladat - \
Készíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 5 x 5-ös mezőben az alábbi alakzatot!

O . . . .
. O . . .
. . O . .
. . . O .
. . . . O

"""

for i in range(5):
    for j in range(5):
        print(f"{i}{j}", end=" ")
    print()










# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print("O ", end='')
#         else:
#             print(". ", end='')
#     print()


