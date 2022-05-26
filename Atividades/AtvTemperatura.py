print("Conversor de temperatura")

temperatura_c = float(input("Digite a temperatura em Celsius:"))

temperatura_f = (1.8 * temperatura_c) + 32 
temperatura_k = temperatura_c + 273

print(f"A temperatura em Fahrenheit é: {temperatura_f}°F")
print(f"A temperatura em Kelvin é: {temperatura_k}K")