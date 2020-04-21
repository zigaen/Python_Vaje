SKRITA_STEVILKA = 12
cifra = 0

while cifra != SKRITA_STEVILKA:
    cifra = int(input("Vnesi stevilko med 1 in 20! : "))

    if cifra == SKRITA_STEVILKA:
        print("Zadel si iskano številko!")
    else:
        print("Daj ugibaj še enkrat! Stevilka ni enaka :"+ str(cifra))