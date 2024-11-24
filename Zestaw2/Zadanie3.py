def rzymskie_na_arabskie(rzymskie):
    # Mapowanie znaków rzymskich na ich wartości arabskie
    mapa_rzymska = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    # Sprawdzanie, czy liczba zawiera tylko prawidłowe znaki
    dozwolone_znaki = set(mapa_rzymska.keys())
    if not all(c in dozwolone_znaki for c in rzymskie):
        raise ValueError("Błąd: Niepoprawny format liczby rzymskiej. Zawiera nieznane symbole.")
    
    # Sprawdzanie poprawności liczby rzymskiej pod kątem sekwencji
    if 'IIII' in rzymskie or 'VV' in rzymskie or 'XXXX' in rzymskie or 'LL' in rzymskie or 'CCCC' in rzymskie or 'DD' in rzymskie or 'MMMM' in rzymskie:
        raise ValueError("Błąd: Niepoprawny format liczby rzymskiej. Zawiera niewłaściwe sekwencje.")
    
    wynik = 0
    poprzednia_wartosc = 0
    
    # Iteracja przez liczby od końca, aby uwzględnić zapisy takie jak IV, IX itd.
    for znak in reversed(rzymskie):
        wartosc = mapa_rzymska[znak]
        
        # Jeśli bieżąca wartość jest mniejsza niż poprzednia, odejmujemy ją
        if wartosc < poprzednia_wartosc:
            wynik -= wartosc
        else:
            wynik += wartosc
        
        poprzednia_wartosc = wartosc

    # Weryfikacja wyniku przez odwrotną konwersję
    if arabskie_na_rzymskie(wynik) != rzymskie:
        raise ValueError("Błąd: Niepoprawny format liczby rzymskiej.")

    return wynik


def arabskie_na_rzymskie(arabskie):
    if not (1 <= arabskie <= 3999):
        raise ValueError("Liczba musi być w zakresie 1-3999")
    
    mapa_arabska = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    rzymska = ""
    for wartosc, symbol in mapa_arabska:
        while arabskie >= wartosc:
            arabskie -= wartosc
            rzymska += symbol

    return rzymska


# Sekcja testowa
if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        # Przykłady konwersji arabskiej na rzymską
        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
        
        # Test błędu (niepoprawny format)
        print(rzymskie_na_arabskie("IIII"))  # Powinno zgłosić wyjątek
        
    except ValueError as e:
        print(e)
