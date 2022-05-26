soma = lambda a,b: a+b
subtracao = lambda a,b: a-b
multiplicacao = lambda a,b: a*b
divisao = lambda a,b: a/b

print("Calculadora Lambda")
print("[1] Soma\n[2] Subtrção\n[3] Multiplicação\n[4] Divisão\n ")
while True:
    op = int(input("Digite uma opção: "))
    if op == 0:
        print("Obrigado por utilizar nossa calculadora!")
        break
    elif str(op) not in "1234":
        print("Opção inválida!")
    else:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        if op == 1: print(soma(a,b))
        elif op == 2: print(subtracao(a,b)) 
        elif op == 3: print(multiplicacao(a,b)) 
        else: print(divisao(a,b)) 