salarioF = float(input("Digite seu salário fixo: "))
vendas = float(input("Digite o valor de vendas: "))

comissao = vendas * 0.04
salarioF += comissao

print(f"Comissão: R$ {comissao:.2f}")
print(f"Salário Final: R$ {salarioF:.2f}")


