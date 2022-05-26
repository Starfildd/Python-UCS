bin = input("Digite um número binário:")
decimal = 0
n = len(bin)-1

for d in bin:
    decimal = decimal + int(d)*2**n
    n = n - 1
    
print(f"O número binario {bin} é igual a {decimal} na base 10")