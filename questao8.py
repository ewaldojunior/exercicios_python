def converter_MB(tam_bytes):
    return int(tam_bytes) / 1048576

dados = []

#uso do with: facilita a escrita de blocos de código que precisam ser finalizados
with open('usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        usuario = linha[:15] #posição na linha
        tam_disk = converter_MB(linha[15:])
        dados.append((usuario, tam_disk))

titulo = '''
ACME Inc.              Uso do espaço em disco pelos usuários
------------------------------------------------------------
Nr.   Usuário            Espaço Utilizado           % do uso
'''

with open('relatorio.txt', 'w') as arquivo:
    tamanho_total_usado = sum([tamanho for _, tamanho in dados]) # list comprehension -> soma tudo e insere numa nova lista
    media = tamanho_total_usado / len(dados)
  
    arquivo.writelines(titulo)

    for id, dado in enumerate(dados, start=1):
        usuario, tam_disk = dado
        arquivo.writelines(f'{id:<4}  {usuario}    {tam_disk:9.2f} MB                {tam_disk / tamanho_total_usado:6.2%}\n')
    
    arquivo.writelines('\n')
    arquivo.writelines(f'Espaço total ocupado: {tamanho_total_usado:.2f} MB\n')
    arquivo.writelines(f'Espaço médio ocupado: {media:.2f} MB')