lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
N = 20 
#Imprimindo a lista original
print("Lista original", lista)
#chamamos de variavel i a posição do elemento na lista criada
for i in range(0, N - 1, 1): 
#chamamos de variavel j a posição imendiatamente após i,ou seja, i + 1
    for j in range(i + 1, N, 1): 
#se elemento na posição i for maior que o da posicao j, troca-se de posição. Se não, mantem.
        if lista[i] > lista[j]: 
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
#para mostrar a lista modificada em ordem crescente.
print("Lista em ordem crescente", lista) 
