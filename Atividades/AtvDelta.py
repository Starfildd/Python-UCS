print("Digite os números de a, b e c:")

a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

D = (b ** 2) - 4 * a * c  

if D < 0:
    print("Conta sem solução")
  
else:  
    x1 = (-b + (D ** 0.5)) / (2*a)
    x2 = (-b - (D ** 0.5)) / (2*a)

    print(f"x1 = {x1}")
    print(f"x2 = {x2}")