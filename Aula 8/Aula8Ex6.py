horaA = float(input("Digite o preço da hora trabalhada: "))
semana = int(input("Digite a quantidade de semanas trabalhadas: "))

salarioB = horaA * semana * 4.5
adicional = salarioB *1 /6
salarioF = salarioB + adicional 

print(f"Salário final: R$ {salarioF:.2f}")