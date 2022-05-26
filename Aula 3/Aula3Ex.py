num = int(input("Digite um número inteiro:"))
d1 = num // 100
d2 = num%100//10 
d3 = num%10
num = d3*100 + d2*10 + d1*1
print(num)