import math

raio = float(input("Digite o raio da circunferência em cm:"))
area = math.pi*raio**2
comprimento = 2*math.pi*raio 

print(f"Área = {area:.2f} cm²")
print(f"Comprimento = {comprimento:.2f} cm²")
