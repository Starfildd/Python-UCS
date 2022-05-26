import math

area = int(input("Digite a área a ser pintada (em m²): "))

qTinta = area/3
qLatas = qTinta/18
qLatas = math.ceil(qLatas)
print(f"Você vai precisar comprar {qLatas} latas ")
print(f"O valor total é de R${qLatas*80}")