idade = int(input("Digite a idade"))

if idade <16:
    categoria = "não eleitor"
elif idade >=18 and idade <= 65:
    categoria = "eleitor facultativo"
else:
    categoria = "eleitor facultativo"
    
print(f"Sua classe eleitoral é {categoria}") 