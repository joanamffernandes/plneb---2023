# EXERCÍCIOS AULA 23 FEVEREIRO

# PARTE 1
# 1. Programa que pergunta ao utilizador o nome e imprime em maiúsculas

def nome():
    nome = input("Inserir nome: ")
    print('Nome em letras maiúsculas:', nome.upper())

#nome()

# 2. Função que recebe array de números e imprime números pares

def pares():
    inserir = input("Inserir números: ")
    lista = [int(num) for num in inserir.split()]
    listap = []
    for i in lista:
        if i % 2 == 0:
            listap.append(i)
    print(listap)

#pares()

# 3. Função que recebe nome de ficheiro e imprime linhas do ficheiro em ordem inversa

def ficheiro(nome_ficheiro):
    with open(nome_ficheiro, 'r') as ficheiro:
        linhas = ficheiro.readlines()
        for linha in reversed(linhas):
            print(linha.rstrip())

#ficheiro("file.txt")

# 4. Função que recebe nome de ficheiro e imprime o número de ocorrências das 10 palavras mais frequentes no ficheiro

def freq(nome_ficheiro):
    contador = {}
    with open(nome_ficheiro, 'r') as ficheiro:
        for linha in ficheiro:
            palavras = linha.strip().split()
            for palavra in palavras:
                contador[palavra] = contador.get(palavra, 0) + 1
    ordem = sorted(contador, key=contador.get, reverse=True)
    for i in range(10):
        palavra = ordem[i]
        freq = contador[palavra]
        print(f'{palavra}: {freq}')

#freq("file.txt")

# 5. Função que recebe um texto como argumento e o 'limpa': separa palavras e pontuação com espaços, converta para minúsculas, remove acentuação de carateres, etc

from unidecode import unidecode

def limpa():
    texto = input(('Inserir texto: '))
    texto = texto.lower()
    texto = unidecode(texto)
    print(texto)

limpa()


# PARTE 2
# 1. Given a string "s", reverse it

def reverse():
    s = input("Introduzir string: ")
    print(s[::-1])

#reverse()

# 2. Given a string "s", returns how many "a" and "A" characters are present in it

def contagem():
    s = input("Introduzir string: ")
    contaa = 0
    contaA = 0
    for i in s:
        if i == "a":
            contaa += 1
    for j in s:
        if j == "A":
            contaA += 1

    print("a:", contaa)
    print("A:", contaA)

# contagem()

# 3. Given a string "s", returns the number of vowels there are present in it

def vogais():
    s = input("Introduzir string: ")
    contagem = 0
    for i in s:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            contagem += 1
    print(contagem)

#vogais()

# 4. Given a string "s", convert it into lowercase

def minuscula():
    s = input("Introduzir string: ")
    print(s.lower())

#minuscula()

# 5. Given a string "s", convert it into uppercase

def maiuscula():
    s = input("Introduzir string: ")
    print(s.upper())

#maiuscula()