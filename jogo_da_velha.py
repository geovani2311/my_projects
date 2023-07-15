# PROJETO EM DESEVOLVIMENTO...

import random
import time
import os

# VARIAVEIS GLOBAIS

def jogo():
    lista = [[" "," "," "],[" "," "," "],[" "," "," "]]
    print("Bem vindo ao jogo da velha\n")
    print("Escolha a posição da coluna e linha para assinalar, sendo 0 a primeira coluna e 0 a primeira linha")
    time.sleep(1)
    print("Jogo começa em: ")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1\n")
    
    print("  " + lista[0][0] +" ║ "+ lista[0][1] +" ║ "+ lista[0][2])
    print("═════════════")
    print("  " + lista[1][0] +" ║ "+ lista[1][1] +" ║ "+ lista[1][2])
    print("═════════════")
    print("  " + lista[2][0] +" ║ "+ lista[2][1] +" ║ "+ lista[2][2])

#DEFINIR ESSA AÇÃO COMO CLASSE USUARIO
    coluna = int(input("Digite a coluna: "))
    linha =  int(input("Digite a linha: "))
    resultado_usuario = str(coluna) + "," + str(linha)
        
    lista[coluna][linha] = "X"
    os.system('cls')
    print("  " + lista[0][0] +" ║ "+ lista[0][1] +" ║ "+ lista[0][2])
    print("═════════════")
    print("  " + lista[1][0] +" ║ "+ lista[1][1] +" ║ "+ lista[1][2])
    print("═════════════")
    print("  " + lista[2][0] +" ║ "+ lista[2][1] +" ║ "+ lista[2][2])


#DEFINIR CLASSE PARA MAQUINA NA QUAL PEGA ATRIBUTOS E MÉTODOS DO USUARIO

    while resultado_maquina == resultado_usuario:

        numero_aleatorio_linha = random.randint(0,2)
        numero_aleatorio_coluna = random.randint(0,2) 

        resultado_maquina = str(numero_aleatorio_coluna) + "," + str(numero_aleatorio_linha)
        lista[numero_aleatorio_linha][numero_aleatorio_coluna] = "O"

        print()
        print("  " + lista[0][0] +" ║ "+ lista[0][1] +" ║ "+ lista[0][2])
        print("═════════════")
        print("  " + lista[1][0] +" ║ "+ lista[1][1] +" ║ "+ lista[1][2])
        print("═════════════")
        print("  " + lista[2][0] +" ║ "+ lista[2][1] +" ║ "+ lista[2][2])

jogo()
