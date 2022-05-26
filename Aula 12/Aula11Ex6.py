notas = []
nota = int(input("Digite a quantidade de notas: "))

while True: 
    nota = float(input(f"Digite a nota: (-1 para sair) "))
    if nota == -1: break
    else: notas.append(nota)
    
media = sum(notas)/len(notas)
print(f"A média é {media:.2f}")

