print("***Votação para o melhor dia de realização das lives***");

segunda_feira = float(input("Quantos votos Segunda-feira recebeu?\n"))
terca_feira = float(input("E quantos votos Terça-feira?\n"))
quarta_feira = float(input("E quantos votos Quarta-feira?\n"))
quinta_feira = float(input("E quantos votos Quinta-feira?\n"))
sexta_feira = float(input("E quantos votos Sexta-feira?\n"))

if segunda_feira > terca_feira and segunda_feira > quarta_feira and segunda_feira > quinta_feira and segunda_feira > sexta_feira:
    print("O dia escolhido foi Segunda-Feira com {0:.0f} votos".format(segunda_feira))

elif terca_feira > segunda_feira and terca_feira > quarta_feira and terca_feira > quinta_feira and terca_feira > sexta_feira:
    print("O dia escolhido foi Terça-Feira com {0:.0f} votos".format(terca_feira))

elif quarta_feira > segunda_feira and quarta_feira > terca_feira and quarta_feira > quinta_feira and quarta_feira > sexta_feira:
    print("O dia escolhido foi Quarta-Feira com {0:.0f} votos".format(quarta_feira))

elif quinta_feira > segunda_feira and quinta_feira > terca_feira and quinta_feira > quarta_feira and quinta_feira > sexta_feira:
    print("O dia escolhido foi Quinta-Feira com {0:.0f} votos".format(quinta_feira))

elif sexta_feira > segunda_feira and sexta_feira > terca_feira and sexta_feira > quarta_feira and sexta_feira > quinta_feira:
    print("O dia escolhido foi Sexta-Feira com {0:.0f} votos".format(sexta_feira))

else:
    print("Houve um empate, os resultados foram {} votos para Segunda-Feira, {} votos para Terça-feira, {} votos para Quarta-feira, {} votos para Quinta-Feira e {} votos para Sexta-Feira".format(segunda_feira, terca_feira, quarta_feira, quinta_feira, sexta_feira))