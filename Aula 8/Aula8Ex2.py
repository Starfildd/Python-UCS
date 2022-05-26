download = float(input("Digite o tamanho do arquivo em MB: "))
velocidadeI = float(input("Digite a velocidade da sua internet (Mbps): "))

tempo = download/velocidadeI
min = tempo //60
seg = tempo %60
print(f"Tempo de download: {min} minutos e {seg} segundos.")



