import time

def pasek_postepu(n):
    for i in range(n + 1): 
        
        ile_znakow = i * 50 // 100  
        pasek = "=" * ile_znakow + "-" * (50 - ile_znakow)  

      
        print(f"|{pasek}| {i}%", end="\r")
        time.sleep(0.05)  

    print()  

#np.
pasek_postepu(90)
