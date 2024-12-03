def bin_to_dec(binarni_cislo):
    """
    Převádí binární číslo na decimální. Podporuje vstup jako řetězec (str) nebo celé číslo (int).
    """
    if isinstance(binarni_cislo, int):
        binarni_cislo = str(binarni_cislo)
    

    return int(binarni_cislo,2)

# Testovací funkce
def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21

print (bin_to_dec(10011101))
# Spuštění testů

test_funkce()
print("Všechny testy prošly!")
