import math

#print("O peso de sua bagagem é permitido?")
#pesoBagagem = input("Qual o peso de sua bagagem? ")
#if int(pesoBagagem) <= 18:
#    print ("Pode embarcar! Boa viagem!")
#else:
#    print("Não pode embarcar! Dirija-se ao balcão para mais informações.")

#print("***Ajudando o professor***");
#emailAluno = input("Informe o e-mail do aluno: ");
#notaSemestral = input("Informe a nota semestral: ");
#if float(notaSemestral) > 8.5:
#    print("ENVIANDO E-MAIL PARA {}".format(emailAluno));

#print("***Com que roupa eu vou?***");
#valorCompra = input("Informe o valor da compra: ");
#cupom = input("Digite o cupom de desconto: ");
#if cupom.upper() == "NIVER10":
#    valorFinal = float(valorCompra) * 0.9;
#else:
#    valorFinal = float(valorCompra);
#    print("CUPOM INVÁLIDO");
#print("O valor da final da compra é {}".format(valorFinal))

a = float(input("Informe o valor de A: "));
b = float(input("Informe o valor de B: "));
c = float(input("Informe o valor de b: "));

delta = b * b - 4 * a * c
print(delta)
if delta > 0.0:
    x1 = (-b + math.sqrt(delta)) / (2 * a);
    x2 = (-b - math.sqrt(delta)) / (2 * a);
    print("Para a equação {}x² + {}x + {} = 0, obtivemos os seguintes valores: x1 = {} e x2 = {}".format(a, b, c, x1, x2));
else:
    print("Para a equação {}x² + {}x + {} = 0, não existem valores reais para x".format(a, b, c))