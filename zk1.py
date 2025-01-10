# Příklad 1: Práce s podmínkami a řetězci
# Zadání:
# Napište funkci `process_strings`, která přijme seznam řetězců. 
# Funkce vrátí nový seznam, který obsahuje pouze řetězce delší než 3 znaky, převedené na velká písmena.
# Pokud seznam obsahuje řetězec "STOP", ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

def process_strings(strings):
         # vytvoření nového seznamu
    result = []

    # procházení všech řetězců
    for string in strings:
        
        if string == "STOP":
            #ukonceni pomoci break,kdyz stop
            break

        #  řetězec , pokud je delší než 3 znaky
        if len(string) > 3:
            result.append(string.upper())
            #doddani velkych pismen
    return result
    pass

# Pytest testy pro Příklad 2
def test_process_strings():
    assert process_strings(["abc", "abcd", "STOP", "efgh"]) == ["ABCD"]
    assert process_strings(["hello", "world", "STOP", "python"]) == ["HELLO", "WORLD"]
    assert process_strings(["hi", "ok", "go"]) == []
    assert process_strings(["code", "test", "debug"]) == ["CODE", "TEST", "DEBUG"]