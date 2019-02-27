import random

def imprime(A):  #Função para imprimir a matriz do jogador

    print(" *__*Campo Minado*__* \n")
    print("0       1       2       3       4       5       6       7       8       9")
    print()
    for i in range(matriz):
        for j in range(matriz):
            print(A[i][j], end="\t")
        print()
    print()

#Cria as matrizes A e B

matriz = 10

B = [None]*matriz

for i in range(matriz):
    B[i] = [0] * matriz

for i in range(matriz):
    for j in range(matriz):
        B[i][j] = 0

A = [None]*matriz

for i in range(matriz):
    A[i] = [0] * matriz

for i in range(matriz):
    for j in range(matriz):
        A[i][j] = '-'


def bombas(B):  #Põe as bombas no tabuleiro (matriz B)

    bombas = 15

    for t in range (bombas):
        i = random.randint(0, 9)
        j = random.randint(0, 9)

        while B[i][j] == '#':
            i = random.randint(0, 9)
            j = random.randint(0, 9)

        B[i][j] = '#'

def valid(B,i,j): #Valida se a cell está dentro da matriz

    matriz = 10
        
    return i >= 0 and i < matriz and j >= 0 and j < matriz

def valid2(B,i,j): #Valida se a cell é uma bomba ou não
    
    if B[i][j] == '#':
        return False
    else:
        return True

def vizinhos(B): #Acha o valor para cada cell de acordo com o posicionamento das bombas

    matriz = 10
    
    for i in range (matriz):
        for j in range (matriz):
            if B[i][j] == '#':
                if valid(B,i-1, j) == True:
                    if valid2(B,i-1, j) == True:
                        B[i-1][j] += 1
                if valid(B,i+1, j) == True:
                    if valid2(B,i+1, j) == True:
                        B[i+1][j] += 1
                if valid(B,i, j+1) == True:
                    if valid2(B,i, j+1) == True:
                        B[i][j+1] += 1
                if valid(B,i, j-1) == True:
                    if valid2(B,i, j-1) == True:
                        B[i][j-1] += 1
                if valid(B,i-1, j+1) == True:
                    if valid2(B,i-1, j+1) == True:
                        B[i-1][j+1] += 1
                if valid(B,i-1, j-1) == True:
                    if valid2(B,i-1, j-1) == True:
                        B[i-1][j-1] += 1
                if valid(B,i+1, j+1) == True:
                    if valid2(B,i+1, j+1) == True:
                        B[i+1][j+1] += 1
                if valid(B,i+1, j-1) == True:
                    if valid2(B,i+1, j-1) == True:
                        B[i+1][j-1] += 1
                        
#Abre espaços vazios
def abrirvazios(i,j,B,A):
    A[i][j] = 0
    for n in range(i-1,i+2, 1):
        for m in range(j-1,j+2,1):
            if (n>= 0 and n <=9 and m >=0 and m<=9):
                if (B[n][m] == 0 and A[n][m] != 0):
                    abrirvazios(n,m,B,A)
                elif(B[n][m] >=1 and B[n][m] <=9):
                    A[n][m]= B[n][m]
#
           
                
def entrada(B):     #Dá opção de ações, recebe as entradas e verifica o que são no tabuleiro versão dev. 
    game = True
    cont_bombas_falso = 15
    cont_bombas_real = 15
    while game == True:

        tipo_entrada = input("Selecione o tipo de entrada desejada, F para bandeira e S para selecionar ação: ")

        while tipo_entrada != 'S' and tipo_entrada != 's' and tipo_entrada != 'f' and tipo_entrada != 'F':
            tipo_entrada = input("Input inválido. Selecione o tipo de entrada desejada, F para bandeira e S para selecionar ação: ")

        if tipo_entrada == 'S' or tipo_entrada == 's':
            
            print("Selecione a coordenada desejada para ação (x,y): ")
            i = int(input("x: "))
            while i < 0 or i > 9:
                i = int(input("Input inválido. Digite um número entre 0 e 9 para seu x: "))
            j = int(input("y: "))
            while j < 0 or j > 9:
                j = int(input("Input inválido. Digite um número entre 0 e 9 para seu y: "))

            print()


            if B[i][j] == '#':
                print("Acertou uma Bomba. Game Over.")
                imprime(B)
                game = False

            elif B[i][j] == 0:
                abrirvazios(i,j,B,A)
                imprime(A)
                game = True
                print("Bombas restantes: ",cont_bombas_falso)

            else:
                A[i][j] = B[i][j]
                imprime(A)
                game = True
                print("Bombas restantes: ",cont_bombas_falso)
                


        elif tipo_entrada == 'f' or tipo_entrada == 'F':

            print("Seleciona a coordenada desejada para bandeira (x,y): ")
            i = int(input("x: "))
            while i < 0 or i > 9:
                i = int(input("Input inválido. Digite um número entre 0 e 9 para seu x: "))
            j = int(input("y: "))
            while j < 0 or j > 9:
                j = int(input("Input inválido. Digite um número entre 0 e 9 para seu y: "))
            print("\n")


            if B[i][j] == '#':

                cont_bombas_real -= 1

            if A[i][j] == 'F':

                print("Já está marcado com uma bandeira.")
                print("Bombas restantes: ",cont_bombas_falso)
                print()

                imprime(A)
                   
                game = True
            
            elif A[i][j] != 'F':

                A[i][j] = 'F'

                imprime(A)
                print()
                cont_bombas_falso -= 1
                print("Bombas restantes: ",cont_bombas_falso)

                game = True

            if cont_bombas_real == 0:
                
                print("Todas as bombas foram eliminadas! Você ganhou!")
                game = False

def playgame(): #Função principal(main), chama todas as outras 
    print("O jogo é Campo Minado. Coloque a bandeira em todas as 15 bombas para ganhar o jogo. \nPara selecionar um cell digite S para ação e F para marcar uma bandeira. \nX e Y estão entre 0 e 9.")
    print()
    matriz = 10
    
    bombas(B)
    vizinhos(B)
    imprime(A)
    entrada(B)

playgame()

