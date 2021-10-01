ganho_hr = float(input("Digite quanto você ganha por hora: "))
hrs_trab = float(input("Digite quantas horas você trabalha no mês: "))

salario_bruto = ganho_hr * hrs_trab
IR = (salario_bruto * 11)/100
INSS = (salario_bruto * 8)/100
sindicato = (salario_bruto * 5)/100
salario_liquido = salario_bruto - (INSS + sindicato + IR)

print(f"O salário bruto é: R${salario_bruto}")
#print(f"O valor pago de Imposto de Renda foi de: R${IR}")
print(f"O valor pago ao INSS foi de: R${INSS}")
print(f"O valor pago ao sindicato foi de: R${sindicato}")
print(f"O salário líquido é: R${salario_liquido}")