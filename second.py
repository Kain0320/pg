def cislo_text(cislo):
    nact = {11: "jedenact", 12: "dvanact", 13: "třinact", 14: "čtrnact", 15: "patnact", 16: "šestnact", 17: "sedumnact", 18: "osmnact", 19: "devatenact" }
    desitky = {1: "desat", 2: "dvacet", 3: "tricet", 4:"čtřicet", 5: "padesat", 6: "sestdesat", 7: "sudumdesat", 8: "osmdesat", 9: "devadesat"}
    jednotky = {1: "jedna", 2: "dva", 3:"tri", 4: " čtři", 5: "pet", 6: "sest", 7: "sedum", 8: "osm", 9:"devat"}
    cislo = int(cislo)  
    if cislo ==0:
        return  "nula"
    elif cislo == 100:
        return "sto"
    elif cislo >= 11 and cislo <= 19:
        return nact[cislo]
    else:
        d = cislo // 10
        j = cislo % 10
        vysledek = desitky[d]
        if j !=0:
            vysledek += " " + jednotky[j]
        return vysledek
        
if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)