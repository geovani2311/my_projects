import os
import random

print("▁ ▂ ▃ ▄ ▅ ▆ ▇ ▌　Pedra Papel e Tesoura  ▌ ▇ ▆ ▅ ▄ ▃ ▂ ▁")

#variaveis globais
voce = 0
maquina = 0
lista = ['PEDRA','PAPEL','TESOURA']

def jogo():
    global voce, maquina, lista
    while True:
        try:
            print()
            print("PLACAR:")
            print("Você: {}".format(voce))
            print("maquina: {}".format(maquina))
            print()  
            print("Escolha seu lance:")
            print("0-Papel | 1 - Pedra | 2 - Tesoura")
            print()       
            lance = int(input())
            lance_da_maquina = random.randint(0,2)

            #SE ESCOLHER PAPEl
            if lance == 0 and lance_da_maquina == 0:
                print("Você escolheu {}".format(lista[lance]))
                print("A maquina escolheu {} ".format(lista[lance_da_maquina]))
                print("Empate")
            elif lance == 0 and lance_da_maquina == 1:
                print("Você escolheu {} ".format(lista[lance]))
                print("A maquina escolheu {} ".format(lista[lance_da_maquina]))
                print("Você ganhou")
                voce = voce + 1
            elif lance == 0 and lance_da_maquina == 2:
                print("Você escolheu {} ".format(lista[lance]))
                print("A maquina escolheu {} ".format(lista[lance_da_maquina]))
                print("Maquina ganhou")
                maquina = maquina + 1

            #SE ESCOLHER PEDRA
            elif lance == 1 and lance_da_maquina == 1:
                print("Você escolheu {}".format(lista[lance]))
                print("A maquina escolheu {} ".format(lista[lance_da_maquina]))
                print("Empate")
            elif lance == 1 and lance_da_maquina == 2:
                print("Você escolheu {} ".format(lista[lance]))
                print("A maquina escolheu {} ".format(lista[lance_da_maquina]))
                print("Você ganhou")
                voce = voce + 1
            elif lance == 0 and lance_da_maquina == 0:
                print("Você escolheu {} ".format(lista[lance]))
                print("A maquina escolheu {} ".format(lista[lance_da_maquina]))
                print("Maquina ganhou")
                maquina = maquina + 1

            #SE ESCOLHER TESOURA
            elif lance == 2 and lance_da_maquina == 2:
                print("Você escolheu {}".format(lista[lance]))
                print("A maquina escolheu {} ".format(lista[lance_da_maquina]))
                print("Empate")
            elif lance == 2 and lance_da_maquina == 0:
                print("Você escolheu {} ".format(lista[lance]))
                print("A maquina escolheu {} ".format(lista[lance_da_maquina]))
                print("Você ganhou")
                voce = voce + 1
            elif lance == 2 and lance_da_maquina == 1:
                print("Você escolheu {} ".format(lista[lance]))
                print("A maquina escolheu {} ".format(lista[lance_da_maquina]))
                print("Maquina ganhou")
                maquina = maquina + 1
            else:
                print()
        except Exception as e:
            print(e)

        jogar_novamente = int(input("Deseja jogar novamente? Sim-1 | Não-2 "))
        if jogar_novamente == 1:
            os.system('cls')
            print()
        else:
            os.system('cls')
            break
jogo()