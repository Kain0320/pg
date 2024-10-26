def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):

    typ = figurka["typ"]
    pozice = figurka["pozice"]
    x, y = pozice
    cx, cy = cilova_pozice

    
    if not (1 <= cx <= 8 and 1 <= cy <= 8):
        return False

    
    if cilova_pozice in obsazene_pozice:
        return False

    if typ == "pěšec":
        
        if cx == x and cy == y + 1 and cilova_pozice not in obsazene_pozice:
            return True
        if x == 2 and cx == x and cy == y + 2 and (x, y + 1) not in obsazene_pozice and cilova_pozice not in obsazene_pozice:
            return True

    elif typ == "jezdec":
        #Pohyb L  tvar
        if (abs(cx - x), abs(cy - y)) in [(2, 1), (1, 2)]:
            return True

    elif typ == "věž":
        # Pohyb věže
        if cx == x or cy == y:
            if cx == x:
                for i in range(min(y, cy) + 1, max(y, cy)):
                    if (x, i) in obsazene_pozice:
                        return False
            else:
                for i in range(min(x, cx) + 1, max(x, cx)):
                    if (i, y) in obsazene_pozice:
                        return False
            return True

    elif typ == "střelec":
        # Pohyb střelce
        if abs(cx - x) == abs(cy - y):
            dx = 1 if cx > x else -1
            dy = 1 if cy > y else -1
            for i in range(1, abs(cx - x)):
                if (x + i * dx, y + i * dy) in obsazene_pozice:
                    return False
            return True

    elif typ == "dáma":
        # Pohyb dámy (kombinace věže a střelce)
        if cx == x or cy == y:
            if cx == x:
                for i in range(min(y, cy) + 1, max(y, cy)):
                    if (x, i) in obsazene_pozice:
                        return False
            else:
                for i in range(min(x, cx) + 1, max(x, cx)):
                    if (i, y) in obsazene_pozice:
                        return False
            return True
        elif abs(cx - x) == abs(cy - y):
            dx = 1 if cx > x else -1
            dy = 1 if cy > y else -1
            for i in range(1, abs(cx - x)):
                if (x + i * dx, y + i * dy) in obsazene_pozice:
                    return False
            return True

    elif typ == "král":
        # Pohyb krále (jedno pole ve všech směrech)
        if abs(cx - x) <= 1 and abs(cy - y) <= 1:
            return True

    return False

# Testovací příklady
if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
