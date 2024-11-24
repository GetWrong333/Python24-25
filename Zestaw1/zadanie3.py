import time
from datetime import datetime

# Napisać program, który będzie wyświetlał bieżący czas (tak ma to wyglądać: ►    14:48:31   ◄),
# aktualizowany dynamicznie. Czas można odczytać  na wiele sposobów, użyjmy moduł  datetime,
# wtedy, bieżący punkt w czasie dostaniemy: now = datetime.now() i za pomocą składowych now.hour,
# now.minute, now.second mamy potrzebne wartości. Przy czym dla sekund należy sprytnie podmienić 
# sekundy w zakresie 0..9 tak, żeby przed nimi wyświetlało się zero (np. nie 5,tylko 05). Znaczki na początku
# i końcu mają kod chr(16) i chr(17). Zegar musi być wyświetlany w nieskończonej pętli funkcją print(),
# argument end='\r' zapewni nadpisywanie. Potrzebne jest jeszcze (z modułu time) wołanie czegoś typu
# time.sleep(0.5) w pętli, żeby niepotrzebnie nie odświeżać zbyt często bieżącego odczytu czasu.
# Wymagania formalne Użyć  plik ZADANIE3/zadanie3.py w repozytorium GitHub Classroom
# do uzupełnienia swoim kodem. Program będzie uruchomiony i oceniony wizualnie, ale jedyny test
# sprawdzi, czy obecna jest  w kodzie funkcja wyswietl_zegar().

spacing = "    "

def wyswietl_zegar():
    time.sleep(0.5)
    now = datetime.now()
    godziny = now.hour
    minuty = now.minute
    sekundy= now.second
    
    if sekundy > 9:
        print(chr(16),spacing, godziny,":",minuty,":",sekundy,spacing,chr(17),end="\r")
    else:
        print(chr(16),spacing, godziny,":",minuty,":",f"0{sekundy}",spacing,chr(17),end="\r")


        

if __name__ == "__main__":
    while True:
        wyswietl_zegar()
        
