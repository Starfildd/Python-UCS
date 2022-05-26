valorPrestacao = int(input("Digite o valor da prestação: "))
qtdeDias = int(input("Digite a quantidade de dias: "))

multa = int(input("Digite a porcentagem de multa: "))

prestacao = valorPrestacao + (valorPrestacao * (multa/100) * qtdeDias)

print(f"O valor da prestação com multa: {prestacao} ")
