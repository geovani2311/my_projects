import random
import time
import os

class tictactoe:
    #inicializa 
    def __init__(self):
        self.reset() 
        print("Bem vindo ao jogo da velha\n")
        print("Escolha a posição da coluna e linha para assinalar, sendo 0 a primeira coluna e 0 a primeira linha")
        time.sleep(1)
        print("Jogo começa em: ")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1\n")
        
    #printa o tabuleiro
    def print_board(self):
        print("-------------")
        print("  " + self.board[0][0] +" ║ "+ self.board[0][1] +" ║ "+ self.board[0][2])
        print("═════════════")
        print("  " + self.board[1][0] +" ║ "+ self.board[1][1] +" ║ "+ self.board[1][2])
        print("═════════════")
        print("  " + self.board[2][0] +" ║ "+ self.board[2][1] +" ║ "+ self.board[2][2])
        print("-------------")

    #reseta o jogo
    def reset(self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.done = ""

    #verificar quem ganhou ou se teve empate
    def check_win(self):
        dict_win = {}
        for i in ["X", "O"]:
            #horizontal
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]
            #verboard
            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]
            #diaboard
            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][1] == self.board[2][0] == i) or dict_win[i]

        if dict_win["X"]:
            self.done = "X"
            print("X venceu!")
            return
        elif dict_win["O"]:
            print("O venceu!")
            return
        
        #chegando se todos campos da lista estão preenchidos 
        c = 0 
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != "":
                    c = c + 1 
                    break
        if c == 0:
            self.done = "d"
            print("Empate!")
            return

    #jogadas do jogador e prevenindo do jogador de fazer jogadas inválidas    
    def player_move(self):
        invalid_move=True        
        while invalid_move:
            try:
                print("Digite linha: ")
                linha = int(input())
                print("Digite a coluna: ")
                coluna = int(input())

                if linha > 2 or linha < 0 or coluna > 2 or coluna < 0:
                    print("Coordenadas inválidas")

                if self.board[linha][coluna] != " ":
                    print("Posição já preenchida.")
                    continue
            except Exception as e:
                print(e)
                continue

            invalid_move = False
            self.board[linha][coluna] = "X"


    #jogadas do computador
    def computer_move(self):
        list_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    list_moves.append((i, j))
        if len(list_moves) > 0:
            linha, coluna = random.choice(list_moves)
            self.board[linha][coluna] = "O" 


tictactoe = tictactoe()
next = 0 

while next == 0:
    tictactoe.print_board()
    while tictactoe.done == "":
        tictactoe.player_move()
        tictactoe.computer_move()
        os.system("cls")
        tictactoe.print_board()
        tictactoe.check_win()
    print("digite 1 para sair do jogo ou qualquer tecla para jogar novamente")
    next = int(input())
    if next == 1:
        break
    else:
        tictactoe.reset()
        next = 0 