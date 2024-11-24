def rzymskie_na_arabskie(rzymskie):
    # Mapowanie znaków rzymskich na ich wartości arabskie
    mapa_rzymska = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    #czy liczba zawiera tylko prawidłowe znaki
    dozwolone_znaki = set(mapa_rzymska.keys())
    
    # wyjatek gdy napotkamy nieznany symbol
    for znak in rzymskie:
        if znak not in dozwolone_znaki:
            raise ValueError(f"Błąd: Niepoprawny format liczby rzymskiej. Zawiera nieznane symbole: {znak}")
    
    # niedozwolone sekwencje
    niepoprawne_sekwencje = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM', 'IC', 'IL', 'ID', 'IM', 'XD', 'XM']
    for sekwencja in niepoprawne_sekwencje:
        if sekwencja in rzymskie:
            raise ValueError(f"Błąd: Niepoprawny format liczby rzymskiej. Zawiera niewłaściwe sekwencje: {sekwencja}")
    
    wynik = 0
    poprzednia_wartosc = 0
    
    # Iteracja od końca, aby uwzględnic zapisy jak IV, IX, ...
    for znak in reversed(rzymskie):
        wartosc = mapa_rzymska[znak]
        
        # biezaca wartosc jest mniejsza niz poprzednia, to ja odejmujemy 
        if wartosc < poprzednia_wartosc:
            wynik -= wartosc
        else:
            wynik += wartosc
        
        poprzednia_wartosc = wartosc

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

if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        # Przykłady konwersji arabskiej na rzymską
        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
        
    except ValueError as e:
        print(e)
