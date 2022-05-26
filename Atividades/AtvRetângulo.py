print("Calculadora de área e perímetro")

print("Digite os lados, a base e a altura do retângulo:")
n1 = float(input("Digite o primeiro lado:"))
n2 = float(input("Digite o segundo lado:"))
n3 = float(input("Digite o terceiro lado:"))
n4 = float(input("Digite o quarto lado:"))
n5 = float(input("Digite a base:"))
n6 = float(input("Digite a altura:"))

perimetro = n1 + n2 + n3 + n4
area = n5 * n6

print(f"`{n1} + {n2} + {n3} + {n4} = O perímetro do retângulo é: {perimetro}")
print(f"`{n5} * {n6} = A área do retângulo é: {area}")



