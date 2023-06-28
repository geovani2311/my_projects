import random
import time

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
    coluna = int(input("Digite a coluna"))
    linha =  int(input("Digite a linha"))
    
    lista = lista[coluna][linha]
    
    print("  " + lista[0][0] +" ║ "+ lista[0][1] +" ║ "+ lista[0][2])
    print("═════════════")
    print("  " + lista[1][0] +" ║ "+ lista[1][1] +" ║ "+ lista[1][2])
    print("═════════════")
    print("  " + lista[2][0] +" ║ "+ lista[2][1] +" ║ "+ lista[2][2])

jogo()


#DEFINIR CLASSE PARA MAQUINA NA QUAL PEGA ATRIBUTOS E MÉTODOS DO USUARIO
def maquina():
    numero_aleatorio = 1 
    while numero_aleatorio in lista:
        numero_aleatorio = random.randint(0, 8)
        lista[numero_aleatorio] = "O"
        print()
        print(lista[0:3])
        print(lista[3:6])
        print(lista[6:9])
