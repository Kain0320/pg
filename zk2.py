# Příklad 2: Práce s externími daty a výpočty
# Zadání:
# Napište funkci `convert_to_czk`, která:
# 1. Přijme částku (`amount`) jako desetinné číslo a kód měny (`currency`) jako řetězec (např. "USD", "EUR").
# 2. Stáhne aktuální kurzovní lístek z URL:
#    http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt
# 3. Načte příslušný kurz podle zadaného kódu měny a provede převod zadané částky na české koruny (CZK).
# 4. Funkce vrátí výslednou částku v CZK zaokrouhlenou na dvě desetinná místa.
# Pokud zadaná měna v kurzovním lístku neexistuje, vyhoďte výjimku `ValueError`.
import requests

def convert_to_czk(amount, currency):
    # stahovani kurzovního lístku 
    url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt" 
    response = requests.get(url) #ukladani do promenne response
    
    #konrola zda se povedlo stahnout
    if not response.ok:
        raise ConnectionError("Failed to fetch exchange rates.")
    
    
    # jednot radky do sez lines
    lines = response.text.split("\n")
    #men kurz
    exchange_rates = {}

    for line in lines[2:]:  # zac z 3. radku (1 a 2 je hlavicka)
        if line.strip():  # kontrola neni-li prazdny radky
            parts = line.split("|")
            if len(parts) == 5: #konrola spravnosti
                country, currency_name, amount_unit, currency_code, exchange_rate = parts #rozdeli na casti
                amount_unit = int(parts[2]) #textovy format
                exchange_rate = float(parts[4].replace(",", ".")) 
                exchange_rates[currency_code] = exchange_rate / amount_unit #dodani do slovniku
                
    
    # kotrnola zda je měna v seznamu
    if currency not in exchange_rates:
        raise ValueError(f"Currency {currency} not found in the exchange rate list.")
    rate = exchange_rates[currency] 
    result = amount * rate
    return round(result, 2) #zakr na 2 des mista


from unittest.mock import patch, MagicMock

def test_convert_to_czk():
    
    mock_response = """31.10.2025 #237
země|měna|množství|kód|kurz
Austrálie|dolar|1|AUD|14,894
EMU|euro|1|EUR|25,480
USA|dolar|1|USD|23,000
Velká Británie|libra|1|GBP|29,745
"""
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, text=mock_response)

        # Testy převodu
        assert convert_to_czk(100, "USD") == 2300.00
        assert convert_to_czk(50, "EUR") == 1274.00
        assert convert_to_czk(200, "AUD") == 2978.80
        
        # Test neexistující měny
        try:
            convert_to_czk(100, "XYZ")
        except ValueError as e:
            assert str(e) == "Currency XYZ not found in the exchange rate list."
