print("***Exercicio 2***");
print("Desconto de passagens aéreas!");
print("");

tipoDePassagem = float(input("Temos três tipos de passagens: Econômica - R$100 (1), Executiva - R$200 (2) e Primeira Classe - R$300 (3). Escolha número do seu tipo de passagem: "));
passageiros = float(input("Temos descontos progressivos para pacotes! Quantos passageiros serão?"));
print("");

valorEconomica = 100;
valorExecutiva = 200;
valorPrimeiraClasse = 300;

if tipoDePassagem == 1:
    if passageiros == 2:
        valorBruto = valorEconomica * passageiros;
        valorDesconto = valorBruto * 0.03;
        valorLiquido = valorBruto - valorDesconto;
        valorMedio = valorLiquido / passageiros;
        
        print("O valor total de seu pedido é de R${0:.2f}".format(valorBruto));
        print("O valor de seu desconto é de R${0:.2f} (3%)".format(valorDesconto));
        print("O valor final de seu pedido é R${0:.2f}".format(valorLiquido));
        print("Cada passageiro pagará o valor de R${0:.2f}".format(valorMedio));

    elif passageiros == 3:
        valorBruto = valorEconomica * passageiros;
        valorDesconto = valorBruto * 0.04;
        valorLiquido = valorBruto - valorDesconto;
        valorMedio = valorLiquido / passageiros;
        
        print("O valor total de seu pedido é de R${0:.2f}".format(valorBruto));
        print("O valor de seu desconto é de R${0:.2f} (4%)".format(valorDesconto));
        print("O valor final de seu pedido é R${0:.2f}".format(valorLiquido));
        print("Cada passageiro pagará o valor de R${0:.2f}".format(valorMedio));
    
    else:
        valorBruto = valorEconomica * passageiros;
        valorDesconto = valorBruto * 0.05;
        valorLiquido = valorBruto - valorDesconto;
        valorMedio = valorLiquido / passageiros;
        
        print("O valor total de seu pedido é de R${0:.2f}".format(valorBruto));
        print("O valor de seu desconto é de R${0:.2f} (5%)".format(valorDesconto));
        print("O valor final de seu pedido é R${0:.2f}".format(valorLiquido));
        print("Cada passageiro pagará o valor de R${0:.2f}".format(valorMedio));

elif tipoDePassagem == 2:
    if passageiros == 2:
        valorBruto = valorExecutiva * passageiros;
        valorDesconto = valorBruto * 0.05;
        valorLiquido = valorBruto - valorDesconto;
        valorMedio = valorLiquido / passageiros;
        
        print("O valor total de seu pedido é de R${0:.2f}".format(valorBruto));
        print("O valor de seu desconto é de R${0:.2f} (5%)".format(valorDesconto));
        print("O valor final de seu pedido é R${0:.2f}".format(valorLiquido));
        print("Cada passageiro pagará o valor de R${0:.2f}".format(valorMedio));

    elif passageiros == 3:
        valorBruto = valorExecutiva * passageiros;
        valorDesconto = valorBruto * 0.07;
        valorLiquido = valorBruto - valorDesconto;
        valorMedio = valorLiquido / passageiros;
        
        print("O valor total de seu pedido é de R${0:.2f}".format(valorBruto));
        print("O valor de seu desconto é de R${0:.2f} (7%)".format(valorDesconto));
        print("O valor final de seu pedido é R${0:.2f}".format(valorLiquido));
        print("Cada passageiro pagará o valor de R${0:.2f}".format(valorMedio));
    
    else:
        valorBruto = valorExecutiva * passageiros;
        valorDesconto = valorBruto * 0.08;
        valorLiquido = valorBruto - valorDesconto;
        valorMedio = valorLiquido / passageiros;
        
        print("O valor total de seu pedido é de R${0:.2f}".format(valorBruto));
        print("O valor de seu desconto é de R${0:.2f} (8%)".format(valorDesconto));
        print("O valor final de seu pedido é R${0:.2f}".format(valorLiquido));
        print("Cada passageiro pagará o valor de R${0:.2f}".format(valorMedio));

elif tipoDePassagem == 3:
    if passageiros == 2:
        valorBruto = valorPrimeiraClasse * passageiros;
        valorDesconto = valorBruto * 0.1;
        valorLiquido = valorBruto - valorDesconto;
        valorMedio = valorLiquido / passageiros;
        
        print("O valor total de seu pedido é de R${0:.2f}".format(valorBruto));
        print("O valor de seu desconto é de R${0:.2f} (10%)".format(valorDesconto));
        print("O valor final de seu pedido é R${0:.2f}".format(valorLiquido));
        print("Cada passageiro pagará o valor de R${0:.2f}".format(valorMedio));

    elif passageiros == 3:
        valorBruto = valorPrimeiraClasse * passageiros;
        valorDesconto = valorBruto * 0.15;
        valorLiquido = valorBruto - valorDesconto;
        valorMedio = valorLiquido / passageiros;
        
        print("O valor total de seu pedido é de R${0:.2f}".format(valorBruto));
        print("O valor de seu desconto é de R${0:.2f} (15%)".format(valorDesconto));
        print("O valor final de seu pedido é R${0:.2f}".format(valorLiquido));
        print("Cada passageiro pagará o valor de R${0:.2f}".format(valorMedio));
    
    else:
        valorBruto = valorPrimeiraClasse * passageiros;
        valorDesconto = valorBruto * 0.2;
        valorLiquido = valorBruto - valorDesconto;
        valorMedio = valorLiquido / passageiros;
        
        print("O valor total de seu pedido é de R${0:.2f}".format(valorBruto));
        print("O valor de seu desconto é de R${0:.2f} (20%)".format(valorDesconto));
        print("O valor final de seu pedido é R${0:.2f}".format(valorLiquido));
        print("Cada passageiro pagará o valor de R${0:.2f}".format(valorMedio));

else:
    print("Seleção inválida digite novamente!")