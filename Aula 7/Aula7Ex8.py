soma = 0
contador = 0

while True:
    num = int(input("Digite um número inteiro (0 para sair):"))
    soma = soma + num
    contador = contador + 1
    if num == 0:
        break

media = soma/contador
print(f"A média dos números digitados é: {media}")