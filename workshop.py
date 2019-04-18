# Números
inteiro = 123456
real = 1.2345

# Strings
texto1 = 'Python é legal'
texto2 = "Python é amor"
texto3 = '你好世界'

# Booleanas
verdadeiro = True
falso = False

# Listas
lista1 = [1, 2, 'USP', 3, 4, 'Butantã', 5, 6]
elemento = lista1[0]
particao = lista1[3:]
lista1.append(7)
lista1.pop(2)
print(lista1)
lista1.pop(4)
print(lista1)

# Condicionais
if texto1 == 'Python é legal':
    print('É isso aí')
elif texto1 == 'Python é chato':
    print('Teu nariz')
else:
    print('Nada acontece')

falso1 = []
falso2 = ''
falso3 = 0

# Loops
for elem in lista1:
    print(elem, end='-')
print()

for c in texto1:
    print(c, end='-')
print()

# Function
def power(x):
    return x ** 2

# Exercício 1
lista2 = []
for ele in lista1:
    res = power(ele)
    lista2.append(res)
print(lista2)

lista3 = []
for ele in lista1:
    if ele % 2 != 0:
        lista3.append(power(ele))
print(lista3)

def troca(x, y):
    aux = x
    x = y
    y = aux
x = 10
y = 


# Manipulação de string
comprimento = len(texto1)
separado = texto1.split(' ')
separado1 = texto1.split('é')
texto4 = texto1 + ' e me salva sempre'
print(texto4)

# Compreensão de Lista
lista4 = [power(x) for x in lista1]
print(lista4)

lista5 = [power(x) for x in lista1 if x % 2 != 0]
print(lista5)

# Exercício 2
import urllib.request

palavras_url = 'http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
response = urllib.request.urlopen(palavras_url)
palavras = response.read().decode().splitlines()

# with open('palavras.txt', 'r') as f:
#     palavras = f.read().split('\n')

maiusculas = [palavra for palavra in palavras if palavra[0].isupper()]
nomes = [palavra for palavra in maiusculas if not palavra.isupper()]

import random

nomes_completos = [random.choice(nomes) + ' ' + random.choice(nomes) for i in range(10)]

# Dicionário
dicio1 = {}
dicio1['Python'] = 'Foda'
dicio1['Programar'] = 'Legal'
dicio1[2] = 'numero'
dicio1['lista'] = [1, 2, 3]
print(dicio1)

dicio2 = {x: power(x) for x in lista1}
print(dicio2)

dicio3 = {x: y for x, y in zip(lista1, lista2)}
print(dicio3)

# Exercício 3
grau = ['Muito Ruim', 'Ruim', 'Neutro', 'Bom', 'Muito Bom']
classificar = {i: g for i, g in enumerate(grau, start=1)}

notas = [random.randint(1, 5) for i in range(10)]

tabela = {}
tabela['nome'] = nomes_completos
tabela['nusp'] = [random.randint(9000000, 10000000) for i in range(10)]
tabela['notas'] = notas
tabela['classificacao'] = [classificar[nota] for nota in notas]
print(tabela)

# Exercício 4
import csv

with open('alunos.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['nome', 'nusp', 'notas', 'classificacao'])
    for i in range(10):
        writer.writerow([tabela['nome'][i], tabela['nusp'][i], tabela['notas'][i], tabela['classificacao'][i]])
