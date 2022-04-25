print("Cáuculo do bônus");

tipo_de_assinatura = float(input("Qual seu tipo de assinatura?\n1-Basic\n2-Silver\n3-Gold\n4-Platinum\n"));
faturamento_anual = float(input("Qual seu faturamento anual?\n"));

#plano básico tem 30% no bônus do pagamento
if tipo_de_assinatura == 1:
    valor_bonus = faturamento_anual * 0.3
    print("O bônus a ser pago é R${}".format(valor_bonus));

#plano silver tem 20% no bônus do pagamento
elif tipo_de_assinatura == 2:
    valor_bonus = faturamento_anual * 0.2
    print("O bônus a ser pago é R${}".format(valor_bonus));

#plano gold tem 10% no bônus do pagamento
elif tipo_de_assinatura == 3:
    valor_bonus = faturamento_anual * 0.1
    print("o bônus a ser pago é R${}".format(valor_bonus));

#plano platinum tem 5% no bônus do pagamento
elif tipo_de_assinatura == 4:
    valor_bonus = faturamento_anual * 0.05
    print("O bônus a ser pago é R${}".format(valor_bonus));

#outro valor de tipo de assinatura inválida
else:
    print("Opção inválida, digite novamente")