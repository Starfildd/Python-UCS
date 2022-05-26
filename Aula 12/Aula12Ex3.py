def imc(peso, altura):
    res = peso / altura**2
    return(res)

def despedida():
    print("Obrigado por usar este programa!") 
    print("Até logo!")
    
peso = float(input("Dige o peso da pessoa em Kg: "))   
altura = float(input("Digite a altura da pessoa em m: "))   
print("O IMC é: ", imc(peso,altura), "Kg/m²")  
despedida() 