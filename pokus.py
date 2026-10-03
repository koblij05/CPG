def secti(a,b,c):
    vysledek = a+b+c
    return vysledek

def je_delitelne_3(a):
    zbytek = a % 3
    if zbytek == 0:
        vysledek ="Je"
    else:
        vysledek = "Není"
    print(vysledek, "dělitelné 3")

def je_sude(a):
    return a % 2 == 0

    
def factorial(x):
    
    if x == 1:
        return 1
    else:        
        return x * factorial(x-1)

if __name__ == "__main__":
    x = secti(1,2,3)
    print("Výsledek je", x)
    je_delitelne_3(x)
    print("Je sude", je_sude(x))

    vstup = input("Zadej číslo: ")
    print(type(vstup))
    vstup = int(vstup)
    print(type(vstup))

    seznam = [0, 1, 2, "tři"]
    seznam.append(6)
    print(seznam)
    print(seznam.count)
    print(seznam[0])
        
    nemmenySeznam = (0, 1, 2, "tři")
    print(nemmenySeznam)


    mnozina = {0,1,2,2,3}
    print(mnozina)



    print(factorial(10))
