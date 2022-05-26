import trigonometria
cat0 = float(input("Digite o cateto oposto: "))
catA = float(input("Digite o cateto ajacente: "))

print(f"seno =", {trigonometria.seno(cat0, catA)})
print(f"cosseno =", {trigonometria.cosseno(cat0, catA)})
print(f"tangente =", {trigonometria.tangente(cat0, catA)})
