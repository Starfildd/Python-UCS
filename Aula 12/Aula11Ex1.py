salarios = []
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
soma = 0
for i in range(12):
    sal = float(input(f"Digite sue salário no mês {meses[i]}: "))
    #Armazenar salários
    salarios.append(sal)

print(salarios)

for i in range(12):
    soma += salarios[i]
decimo13 = soma/12
umTerco = decimo13/3
print(f"Décimo terceiro salário: R$ {decimo13}")
print(f"Um terço de férias: R$ {umTerco}")

