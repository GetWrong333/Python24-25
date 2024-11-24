import sys

def formatuj(lista):
    wyjscie = ""
    i = 0

    while i<len(lista):
        licznik = 1
        
        n = lista[i]
        
        k = i + 1
        
        while  k<len(lista) and n == lista[k]:
            licznik += 1
            k += 1
            
        wyjscie += str(n)
        if licznik > 1:
            wyjscie += "^" + str(licznik)
       
        if (k != len(lista) and i != len(lista)):
            wyjscie += "*"
        
        i = k  
    return wyjscie

# Funkcja do rozkładania liczby na czynniki pierwsze i formatowania wyniku
def rozklad_na_czynniki(n):
    lista = []
    k = 2
    while(n>1):
        
        while(n%k == 0):
            lista.append(k)
            n = n//k
        k+=1    
    lista = formatuj(lista)
    wyjscie = ""
    i = 0

    while i<len(lista):
        licznik = 1
        
        n = lista[i]
        
        k = i + 1
        
        while  k<len(lista) and n == lista[k]:
            licznik += 1
            k += 1
            
        wyjscie += str(n)
        if licznik > 1:
            wyjscie += "^" + str(licznik)
       
        if (k != len(lista) and i != len(lista)):
            wyjscie += "*"
        
        i = k  
    return wyjscie
          
    






# Główna funkcja programu
#
 #   argv = sys.argv[1:]  # Pobieranie argumentów zewnętrznych (liczby)

   # for arg in argv:
if __name__ == "__main__":
        wynik = rozklad_na_czynniki(1296)
        print(wynik)
        
