salario = float(input("Digite aqui o salário do colaborador: "))
print(f"O salário antes do reajuste foi: R${salario}")

if salario <= 280:
  porc = 20 
  reajuste = (salario * porc)/100
  salario_atual = salario + reajuste

elif salario > 280 and salario <= 700:
  porc = 15
  reajuste = (salario * porc)/100
  salario_atual = salario + reajuste

elif salario > 700 and salario <= 1500:
  porc = 10
  reajuste = (salario * porc)/100
  salario_atual = salario + reajuste

else:
  porc = 5
  reajuste = (salario * porc)/100
  salario_atual = salario + reajuste

print(f"O percentual de aumento foi de {porc}% e o valor aumentado foi de: R${reajuste}")
print(f"O salário após o reajuste ficou: R${salario_atual}")