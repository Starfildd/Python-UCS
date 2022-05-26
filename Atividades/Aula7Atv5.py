masc = 0
fem = 0 
contadorM = 0
contadorF = 0

while True:
    sexo = input("Digite o sexo da pessoa: ")
    altura = float(input("Digite a altura da pesoa em m (0 sair)"))
    if altura == 0: break
    elif sexo in "mM":
        masc += altura
        contadorM += 1
    elif sexo in "fF":
        fem += altura
        contadorF += 1 
    else: print("Sexo inválido!!!")
    
mediaM = masc/contadorM
mediaF = fem/contadorF
print(f"Média das alutras:\nMasculino: {mediaM}\nFeminino: {mediaF}")
