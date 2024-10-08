# Criação de uma lista

frutas = ['maça', 'cereja', 'laranja']

# Adicionando elementos

frutas.append('kiwi') # adiciona ao final
frutas.insert(1, "manga") # insere na posição 1

# Removendo elementos

frutas.remove("banana") # remove pelo valor
del frutas[0]  #remove pelo índice
frutas.pop() #remove e retona o último elemento

# Acessando elementos

print(frutas[2]) # acessa o terceiro elemento
print(frutas[-1]) # acessa o último elemento

# Modificando elementos

frutas[1] = 'abacate' # modifica o elemento na posição 1

# Verificando a existência de um elemento

if 'abacate' in frutas: print('abacate está na lista')

# Tamanho da lista

print("Lista:", frutas)
print(len(frutas)) # retorna o número de elementos na lista

# Combinando listas

vegetais = ['cenoura' 'batata']
comida = frutas + vegetais # combina listas

# Outras operações

frutas.sort # ordena a lista
frutas.reverse # inverte a lista
frutas.count('laranja') # conta quantas vezes um elemento aparece
frutas.index('laranja') # encotra o índice de um elemento
copia_frutas = frutas.copy() # faz uma cópia da lista
frutas.clear() # limpa a lista, removendo todos os elementos 