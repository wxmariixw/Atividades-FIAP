print("Descubra a senha atual do programa")

fatorial = 1
minutos = int(input("Qual a minutagem atual da máquina? "))

for i in range (1, minutos + 1):
    fatorial *= i
print("A senha atual é LIBERDADE{}".format(fatorial))