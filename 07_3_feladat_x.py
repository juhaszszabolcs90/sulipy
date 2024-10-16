"""
3. Feladat - X
Készíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 7 x 7-es mezőben az alábbi alakzatot!

O . . . . . O
. O . . . O .
. . O . O . .
. . . O . . .
. . O . O . .
. O . . . O .
O . . . . . O

"""


def print_coordinates_table():
    for i in range(5):
        for j in range(5):
            print(f"{i}{j}", end=" ")
        print()


def draw_diagonal_cross_with_magic_number():
    for i in range(5):
        for j in range(5):
            if i==j:
                print("O", end=" ")
            elif i+j == 5-1:
                print("O", end=" ")
            else:
                print(".", end=" ")
        print()

def draw_custom_diagonal_cross_without_magic_number():
    table_size=7
    for i in range(table_size):
        for j in range(table_size):
            if i==j:
                print("O", end=" ")
            elif i+j == table_size-1:
                print("O", end=" ")
            else:
                print(".", end=" ")
        print()


print_coordinates_table()
# draw_diagonal_cross_with_magic_number()
# draw_custom_diagonal_cross_without_magic_number()