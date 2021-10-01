def valorPagamento(valor_prestacao, numero_dias):

  if numero_dias > 1:
    valor = valor_prestacao + (valor_prestacao * 3)/100 + (numero_dias * 1)/100
    print(f"R${valor}")
    return valor

  else:
    valor = valor_prestacao
    print(f"R${valor}")
    return valor
    
valores = []
qtd = 0

while True:
  valor_prestacao = float(input("Digite o valor da prestação: "))
  if valor_prestacao == 0:
    break
  numero_dias = int(input("Digite quantos dias estão de atraso: "))

  valores.append(valorPagamento(valor_prestacao, numero_dias))

  qtd = qtd + 1

valor_total = sum(valores)

print("---------------Relatório do dia---------------")
print(f"Foram pagas {qtd} prestações no valor de: R${valores}")
print(f"Valor total das prestações foi de: R${valor_total}")