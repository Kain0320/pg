def je_prvocislo(cislo):
    if cislo <= 1:
        return False
    elif cislo == 2:
        return True
    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    seznam_prvocisel = []
    for cislo in range(2, maximum + 1):
        if je_prvocislo(cislo):
            seznam_prvocisel.append(cislo)
    return seznam_prvocisel

if __name__ == "__main__":
    maximum = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(maximum)
    print(prvocisla)