altura = float(input("Digite sua altura em metros: "))
sexo = input("Qual o seu sexo? m|f: ")

if sexo not in "MmFf":
    print("Valor inválido")
elif sexo == 'm' or sexo == "M":
    peso = (72.7*altura) - 58
else:
    peso = (62.1*altura) - 44.7

print(f"O pessoa ideal dessa pessoa é: {peso:.2f}")
    
    
    
    
    