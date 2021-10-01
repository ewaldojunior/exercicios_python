numero = int(input("Digite um número: "))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = numero // 100

print(f"O número invertido fica: {unidade}{dezena}{centena}")