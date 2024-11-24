def fun(n):
    # Zamiana liczby na binarny zapis, usuwamy prefiks "0b"
    bin_rep = bin(n)[2:]

    max_gap = 0  # Zmienna do przechowywania najdłuższej przerwy
    current_gap = 0  # Zmienna do śledzenia bieżącej przerwy

    # Flaga, która sprawdza, czy zaczęliśmy liczyć przerwy (czy napotkaliśmy pierwszą 1)
    counting = False

    for bit in bin_rep:
        if bit == '1':
            if counting:  # Zakończenie przerwy
                max_gap = max(max_gap, current_gap)
            counting = True  # Rozpoczynamy liczenie od teraz
            current_gap = 0  # Resetujemy długość bieżącej przerwy
        elif counting:
            # Liczymy długość przerwy (ciąg zer)
            current_gap += 1

    return max_gap

# Sekcja testowa
if __name__ == "__main__":
    testy = [
        (9, 2),       # 1001 -> przerwa 2
        (529, 4),     # 1000010001 -> przerwy 4 i 3, wynik 4
        (20, 1),      # 10100 -> przerwa 1
        (15, 0),      # 1111 -> brak przerw
        (1041, 5),    # 10000010001 -> przerwa 5
        (1, 0),       # 1 -> brak przerw
        (2147483647, 0)  # 1111111111111111111111111111111 -> brak przerw
    ]

    for n, expected in testy:
        wynik = fun(n)
        print(f"Reprezentacja binarna {n}: {bin(n)}")
        print(f"fun({n}): {wynik}, oczekiwano: {expected}")
        assert wynik == expected, f"Błąd: dla {n} zwrócono {wynik}, oczekiwano {expected}"

print("Wszystkie testy zakończone sukcesem!")
