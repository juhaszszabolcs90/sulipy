def while_ciklus():
    # felhasznalo_sorszam = 1
    # while felhasznalo_sorszam % 2 != 0:
    #     felhasznalo_sorszam = int(input("Adj meg egy páros számot: "))
        darab_karakter = 1
        felhasznalo_sorszam = 8
        sor = 1
        while sor <= felhasznalo_sorszam / 2:
            oszlop = 1
            while oszlop <= darab_karakter:
                print('O ', end='')
                oszlop = oszlop + 1
            print('')
            darab_karakter = darab_karakter + 1
            sor = sor + 1

        sor = felhasznalo_sorszam / 2
        while sor > 0:
            oszlop = 1
            while oszlop < darab_karakter:
                print('O ', end='')
                oszlop = oszlop + 1
            print('')
            darab_karakter = darab_karakter - 1
            sor = sor - 1





# b)
def for_ciklus():
    user_number = 1
    while user_number % 2 != 0:
        user_number = int(input("Adj meg egy páros számot: "))
        # user_number = 8
        number_of_rows = user_number // 2
        for i in range(1, number_of_rows + 1):
            print(i * "O ")
        for i in range(number_of_rows, 0, -1):
            print(i * "O ")





while_ciklus()
# for_ciklus()







def for_ciklus2():
    user_number = 1
    while user_number % 2 != 0:
        user_number = int(input("Adj meg egy páros számot: "))
        if user_number % 2 == 0:
            number_of_rows = user_number // 2
            for i in range(1, number_of_rows + 1):
                print(i * "O ")
            for i in range(number_of_rows, 0, -1):
                print(i * "O ")


# for_ciklus2()
