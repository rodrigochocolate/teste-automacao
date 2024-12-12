# LE O NOME DE UM ARQUIVO
# LE O NOME DE OUTRO ARQUIVO EXISTENTE OU NÃO
# COPIA O TEXTO DO PRIMEIRO ARQUIVO NO SEGUNDO

print('COLOQUE A EXTENSÃO DO ARQUIVO')
copiado = str(input('Primeiro arquivo: '))
colado = str(input('Segundo arquivo: '))

with open(copiado) as texto, open(colado, 'w') as novo:
    novo.write(texto.read())
