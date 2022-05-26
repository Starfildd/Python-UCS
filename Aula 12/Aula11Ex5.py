lista = []
while True:
    n = int(input(f"Digite o número (0 para sair): "))
    
    if n == 0: break 
    else: lista.append(n)
    
media = sum(lista)/len(lista)
print(f"Média: {media:.2f}")
print(f"Minha lista: {lista}")