import math
sombra = float(input("Digite o comprimento da sombra em cm:"))
angulo = math.radians (float(input("Digite o comprimento da sombra em cm:")))
sombra = float(input("Digite o comprimento da sombra em cm:"))
altura = math.tan(angulo) * sombra

print(f"A altura do prédio e de %.2f cm²" % {altura})

