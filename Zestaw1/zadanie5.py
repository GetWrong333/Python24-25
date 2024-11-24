# Napisz program, w którym dowolny tekst " Hello world! " przesuwa się w terminalu w pionie:
# w dół oraz w jakimś miejscu odbija się i do góry, aż do górnej krawędzi okienka itd.
# Wymagania formalne Użyć  plik ZADANIE5/zadanie5.py w repozytorium GitHub Classroom
# do uzupełnienia swoim kodem. Program będzie uruchomiony i oceniony wizualnie, ale jedyny test
# sprawdzi, czy obecna jest  w kodzie funkcja przesun_tekst_w_pionie(txt, n).

import os
import time

def przesun_tekst_w_pionie(txt, n):
    
    while True:
        kierunek = 1 #-1 w gore 1 w dol
        y = 0
        while y<n:        
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n"*y,txt)
            time.sleep(0.5)
            y+=kierunek
            if y == n-1:
                kierunek = -1
            elif y == 0:
                kierunek = 1
        

            

przesun_tekst_w_pionie("X",7)
        




