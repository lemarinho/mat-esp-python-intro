import matplotlib.pyplot as plt
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
N = 20 

#para criar uma figura em branco
plt.figure() 
#para começar a fazer o gráfico onde x = range(0, N), y = lista e  'oK' indica que o gráfico será feito na cor preta e em circulos.
plt.plot(range(0, N), lista, 'ok')
#para colocar um título no gráfico
plt.title("posiçãoxvalores")
#para colocar um tílulo no eixo x 
plt.xlabel("posição")
#para colocar um título no eixo y
plt.ylabel("valores")
plt.savefig("fig/bubble-inicio.png")
plt.close()

#Imprimindo a lista original
print("Lista original", lista)
ntrocas = 0

#chamamos de variavel i a posição do elemento na lista criada
for i in range(0, N - 1, 1): 
#chamamos de variavel j a posição imendiatamente após i,ou seja, i + 1
    for j in range(i + 1, N, 1): 
#se elemento na posição i for maior que o da posicao j, troca-se de posição. Se não, mantem.
        if lista[i] > lista[j]: 
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
            
            ntrocas = ntrocas + 1
            plt.figure() 
            plt.plot(range(0, N), lista, 'ok')
            plt.title("posiçãoxvalores")
            plt.xlabel("posição")
            plt.ylabel("valores")
            plt.savefig("fig/bubble-troca{}.png".format(ntrocas))
            plt.close()
            
#para mostrar a lista modificada em ordem crescente.
print("Lista em ordem crescente", lista)
#para imprimir os cinco maiores valores, o comando deve conter o elemento de posicao 15 até o 20 ja que o programa le a ultima posiao N+1, contando de 1 em 1.
print ("cinco maiores valores", lista[15:20:1])
#para imprimir os cinco menores valores, o comando deve conter o elemento de posicao 0 ate a 5 ja que o programa le a ultima posicao N+1, contando de 1 em 1.
print ("cinco menores valores", lista[0:5:1])

#para criar uma figura em branco
plt.figure() 
#para começar a fazer o gráfico onde x = range(0, N), y = lista e  'oK' indica que o gráfico será feito na cor preta e em circulos.
plt.plot(range(0, N), lista, 'ok')
#para colocar um título no gráfico
plt.title("posiçãoxvalores")
#para colocar um tílulo no eixo x 
plt.xlabel("posição")
#para colocar um título no eixo y
plt.ylabel("valores")
plt.savefig("fig/bubble-fim.png")
plt.close()


