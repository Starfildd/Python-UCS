turno = input("Digite o seu turno do trabalho (N/D): ")

horas = int(input("Digite a quantidade de horas trabalhadas: "))

if turno == "n" or turno == "N":
    valor = 45
else:
    valor = 37.50
    
salario = valor * horas
print(f"Salário = R$ {salario} ")