import random
import time

# VARIAVEIS GLOBAIS
lista = [" "," "," "," "," "," "," "," "," "]

def jogo():
    print("Bem vindo ao jogo da velha\n")
    print("Escolha a posição da coluna e linha para assinalar, sendo 0 a primeira coluna e 0 a primeira linha")
    time.sleep(1)
    print("Jogo começa em: ")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1\n")
    
    print(lista[0:3])
    print(lista[3:6])
    print(lista[6:9])
    
    coluna = int(input("Digite a coluna"))
    linha = int(input("Digite a linha"))
    jogada = (str(coluna) +","+ str(linha))

    if jogada == "0,0":
        usuario_escolhe = "X"
        lista[0] = usuario_escolhe
        print()
        print(lista[0:3])
        print(lista[3:6])
        print(lista[6:9])

        maquina()

    elif jogada == "0,1":
        usuario_escolhe = "X"
        lista[1] = usuario_escolhe
        print()
        print(lista[0:3])
        print(lista[3:6])
        print(lista[6:9])

    elif jogada == "0,2":
        usuario_escolhe = "X"
        lista[2] = usuario_escolhe
        print()
        print(lista[0:3])
        print(lista[3:6])
        print(lista[6:9]) 

    elif jogada == "1,0":
        usuario_escolhe = "X"
        lista[3] = usuario_escolhe
        print()
        print(lista[0:3])
        print(lista[3:6])
        print(lista[6:9])  

    elif jogada == "1,1":
        usuario_escolhe = "X"
        lista[4] = usuario_escolhe
        print()
        print(lista[0:3])
        print(lista[3:6])
        print(lista[6:9])  

    elif jogada == "1,2":
        usuario_escolhe = "X"
        lista[5] = usuario_escolhe
        print()
        print(lista[0:3])
        print(lista[3:6])
        print(lista[6:9])  

    elif jogada == "2,0":
        usuario_escolhe = "X"
        lista[6] = usuario_escolhe
        print()
        print(lista[0:3])
        print(lista[3:6])
        print(lista[6:9])  

    elif jogada == "2,1":
        usuario_escolhe = "X"
        lista[7] = usuario_escolhe
        print()
        print(lista[0:3])
        print(lista[3:6])
        print(lista[6:9])  

    elif jogada == "2,2":
        usuario_escolhe = "X"
        lista[8] = usuario_escolhe
        print()
        print(lista[0:3])
        print(lista[3:6])
        print(lista[6:9])     

    else:
        print("jogada invalida, recomece o jogo")


def maquina():
    numero_aleatorio = 1 
    while numero_aleatorio in lista:
        numero_aleatorio = random.randint(0, 8)
        lista[numero_aleatorio] = "O"
        print()
        print(lista[0:3])
        print(lista[3:6])
        print(lista[6:9])


jogo()