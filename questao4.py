print("OBS: quando quiser parar, informe -1")

numero = 0
contador = 0
lista_numeros = []

while numero >= 0:
  numero = int(input("Informe um número: "))
  lista_numeros.append(numero)
  contador = contador + 1

contador = contador - 1

lista_numeros.pop(-1)
soma = sum(lista_numeros)
media = soma / contador

print("---------------------------------------------")
print(f"A lista possui {contador} elementos")
print(f"A lista de números é: {lista_numeros}")
print(f"A lista invertida: {sorted(lista_numeros, key=lista_numeros.index, reverse=True)}")
print(f"A soma de elementos da lista é: {soma}")
print(f"A média dos elementos da lista é: {media}")

contador_maior_media = 0
for x in lista_numeros:
  if x > media:
    contador_maior_media = contador_maior_media + 1

contador_menor_sete = 0
for x in lista_numeros:
  if x < 7:
    contador_menor_sete = contador_menor_sete + 1

print(f"Quantidade de valores maiores que a média: {contador_maior_media}")
print(f"Quantidade de valores menores que sete: {contador_menor_sete}")
print(f"---------------Fim do programa---------------")
