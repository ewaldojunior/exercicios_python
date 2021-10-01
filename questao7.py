texto = str(input("Digite um texto: "))

texto_convertido = texto.replace('A', '4').replace('B', '8').replace('C', '[').replace('E', '3').replace('I', '|').replace('J', ']').replace('O', '0').replace('S', '$').replace('T', '7').replace('Z', '2').replace('a', '@').replace('b', '6').replace('g', '9').replace('l', '1').replace('s', '5').replace('t', '+')

print(f'Convertido para LeetSpeak: {texto_convertido}')
