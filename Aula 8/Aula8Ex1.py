carneirinho = 0
contadorC = 0

while True:
    carneirinho = input("Já dormiu? s/n: ")
    if carneirinho in "nN": 
        carneirinho = 0
        contadorC += 1 
    elif carneirinho in "sS":
        break
    
print(f"Você contou {contadorC} carneirinhos")