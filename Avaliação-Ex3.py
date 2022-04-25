print ("Notas dos alunos")

nota_somada = 0

for numero_chamada in range (1, 50, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
    nota_aluno = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {} ".format(numero_chamada)))
    nota_somada = nota_somada + nota_aluno
media_turma_impar = nota_somada/25

print("A média da turma impar é de {} pontos".format(media_turma_impar))

nota_somada = 0

for numero_chamada in range (2, 51, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    nota_aluno = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {} ".format(numero_chamada)))
    nota_somada = nota_somada + nota_aluno
media_turma_par = nota_somada/25

print("A média da turma par é de {} pontos".format(media_turma_par))

if media_turma_impar > media_turma_par:
    print("A turma ímpar obteve a maior média de notas")
elif media_turma_impar < media_turma_par:
    print("A turma par obteve a maior média de notas")
else:
    print("A média de notas entre as duas turmas foram iguais")


