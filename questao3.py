valor_hr = float(input("Informe o valor da hora trabalhada: "))
qtd_hrs = float(input("Informe a quantidade de horas trabalhadas: "))

salario_bruto = valor_hr * qtd_hrs
sindicato = (salario_bruto * 3)/100
fgts = (salario_bruto * 11)/100

print("----------------------------------------------")
print(f"Salário bruto: R${salario_bruto}")
print(f"Sindicato: R${sindicato}")
print(f"FGTS (não descontado no salário): R${fgts}")

if salario_bruto <= 900:
  IR = 0

elif salario_bruto <= 1500:
  IR = (salario_bruto * 5)/100

elif salario_bruto <= 2500:
  IR = (salario_bruto * 10)/100

else:
  IR = (salario_bruto * 20)/100

salario_liquido = salario_bruto - (IR + sindicato)
print(f"Imposto de renda: R${IR}")
print(f"Salário líquido: R${salario_liquido}")

