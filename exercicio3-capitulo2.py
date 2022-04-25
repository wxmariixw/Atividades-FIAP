print("***Exercicio 3***")
print("Cálculo de votos")
print("Insira os votos de cada membro da equipe: ")

playstation = float(input("Quantos votos foram para playstation? "))
xbox = float(input("Quantos votos foram para xbox? "))
nintendo = float(input("Quantos votos foram para nintendo? "))

if playstation > xbox and playstation > nintendo:
    print("O video-game escolhido foi playstation com {} votos".format(playstation))

elif xbox > nintendo and xbox > playstation:
    print("O video-game escolhido foi xbox com {} votos".format(xbox))

else:
    print("O video-game escolhido foi nintendo com {} votos".format(nintendo))