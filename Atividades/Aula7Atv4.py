positivo = 0
negativo = 0
menor = 0 
flag = False
menor = 0

while True:
    num = float(input("Digite um número real (0 sair)"))
    if flag == False:
        menor = num
        flag = True
    elif num < menor:
        menor = num
        
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    else: break

print(f"Menor número digitado {menor}")        
print(f"Menor números positivos {positivo}")        
print(f"Menor número digitado {negativo}")
        
        
        
    