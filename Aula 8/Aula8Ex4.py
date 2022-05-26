soma =0

conta = input("Digite a conta de 4 algarismos: ")


for d in conta:
    soma += int(d)
    
dig = soma % 10

print(dig)