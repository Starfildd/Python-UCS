import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

if a == 0:
    print("Não é equação de segundo grau")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Não há raizes reais")
    elif delta == 0:
        x = (-b + math.sqrt(delta))/2*a
        print(f"x1 = x2 = {x}")
    else:
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b + math.sqrt(delta))/2*a
        print (f"x1 = {x1}\nx2 = {x2}")
        
    