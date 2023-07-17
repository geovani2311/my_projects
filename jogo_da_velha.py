# PROJETO EM DESEVOLVIMENTO...

import random
import time
import os

# VARIAVEIS GLOBAIS

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

    lista = [[" "," "," "],[" "," "," "],[" "," "," "]]

    for i in range(len(lista)): 
        for j in range(len(lista[0])):
            if lista[i][j] == " ":

                print("  " + lista[0][0] +" ║ "+ lista[0][1] +" ║ "+ lista[0][2])
                print("═════════════")
                print("  " + lista[1][0] +" ║ "+ lista[1][1] +" ║ "+ lista[1][2])
                print("═════════════")
                print("  " + lista[2][0] +" ║ "+ lista[2][1] +" ║ "+ lista[2][2])
                print("---------------")

                #JOGADA DO USUARIO
                coluna = int(input("Digite a linha: "))
                linha =  int(input("Digite a coluna: "))
                resultado_usuario = str(coluna) + "," + str(linha)

                lista[coluna][linha] = "X"
                os.system('cls')
                print("  " + lista[0][0] +" ║ "+ lista[0][1] +" ║ "+ lista[0][2])
                print("═════════════")
                print("  " + lista[1][0] +" ║ "+ lista[1][1] +" ║ "+ lista[1][2])
                print("═════════════")
                print("  " + lista[2][0] +" ║ "+ lista[2][1] +" ║ "+ lista[2][2])
                print("---------------")

                #JOGADA DA MAQUINA
                resultado_maquina = 1,1

                while resultado_maquina != resultado_usuario:
                    if resultado_maquina != resultado_usuario:   
                        numero_aleatorio_coluna = random.randint(0,2) 
                        numero_aleatorio_linha = random.randint(0,2)
                        resultado_maquina = str(numero_aleatorio_coluna) + "," + str(numero_aleatorio_linha)
                        lista[numero_aleatorio_coluna][numero_aleatorio_linha] = "O"
                        print()
                        print("  " + lista[0][0] +" ║ "+ lista[0][1] +" ║ "+ lista[0][2])
                        print("═════════════")
                        print("  " + lista[1][0] +" ║ "+ lista[1][1] +" ║ "+ lista[1][2])
                        print("═════════════")
                        print("  " + lista[2][0] +" ║ "+ lista[2][1] +" ║ "+ lista[2][2])
                        os.system('cls')
                        print("---------------")
                        break
                    else:
                        print("invalido")


jogo()  
