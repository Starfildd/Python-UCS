while True:
    num = input("Digite um número inteiro (s para sair): ")
    if num in "sS":
        break
    elif int(num) > 10:
        contador = contador + 1

print(f"Foram digitados {contador} números maiores que 10")
