valor = float(input("Digite o valor da compra: "))

if valor > 200:
    desconto = valor*0.2
else:
    desconto = 0
    
    print("Valor a pagar R$" , valor-desconto)
    