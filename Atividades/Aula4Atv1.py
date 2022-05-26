h = int(input("Digite o valor do tronco da pirâmide: "))
bMenor = int(input("Digite o valor da base menor: "))
bMaior = int(input("Digite o valor da base maior: "))

volume = h/3* (bMaior**2 + bMenor**2 + (bMaior**2 * bMenor**2)**0.5)

print(f"O valor da expressão é: {volume}")

