def cislo_text(cislo):
    cisla_texty = {
        0: "nula",
        1: "jedna",
        15: "patnáct",
        25: "dvacet pět",
        50: "padesát",
        100: "sto"
    }
    
    cislo = int(cislo)  
    if cislo in cisla_texty:
        return cisla_texty[cislo]
    else:
        return "Číslo není podporováno"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)