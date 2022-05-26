notaP1 = float(input("Digite a primeira nota parcial: "))
notaP2 = float(input("Digite a segunda nota parcial: "))

media = (notaP1 + notaP2) /2

if media >= 9:
    print("conceito: A\nMensagem: Aprovado") 
elif media >= 7.5:
    print("conceito: B\nMensagem: Aprovado")
elif media >= 6.0:
    print("conceito: C\nMensagem: Aprovado")
elif media >=4.0:
    print("conceito: D\nMensagem: Reprovado")
else:
    print("conceito: E\nMensagem: Reprovado")
    
print(f"O conceito da sua nota é: {conceito}")