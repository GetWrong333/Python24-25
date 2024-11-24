def rysuj_miarke(dlugosc):
    # Tworzenie pierwszej linii z pionowymi kreskami
    pelna_miarka = "|"
    for n in range(dlugosc):
        pelna_miarka += "....|"
    
    pelna_miarka += "\n"
    
    # Tworzenie drugiej linii z liczbami
    pelna_miarka += "0"
    for i in range(1, dlugosc + 1):
        # Dostosowanie odstępu w zależności od długości liczby
        if i < 10:
            pelna_miarka += "    "  # 4 spacje
        elif i < 100:
            pelna_miarka += "   "   # 3 spacje
        else:
            pelna_miarka += "  "    # 2 spacje
        pelna_miarka += str(i)
    
    return pelna_miarka  # Zwracanie wyniku jako string

# Funkcja główna do testowania
def main():
    dlugosc_miarki = 30  # Możesz zmienić długość miarki
    miarka = rysuj_miarke(dlugosc_miarki)
    print(miarka)

if __name__ == "__main__":
    main()
