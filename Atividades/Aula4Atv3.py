print("Conversão de anos, meses e dias para dias")

anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite sua idade em meses: "))
dias = int(input("Digite sua idade em dias: "))

ano = 365 * anos
mes = meses * 30 
idade = ano + mes + dias

print(f"Sua idade é: {idade}")


