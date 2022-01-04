#пишем сапера, всем похуй
import random
from random import randint as rd
import os

class Game:
    def __init__(self, size, bomb):
        self.field = []
        self.size = size
        self.bomb = bomb
        for i in range(size):
            self.field.append([0]*size)
        for i in range(bomb):
            y = rd(0, size - 1)
            x = rd(0, size-1)
            while (self.field[y][x] == '¤'):
                y = rd(0, size - 1)
                x = rd(0, size-1)
            self.field[y][x] = '¤'
            for a in range(-1, 2):
                for b in range(-1, 2):
                    try:
                        if (y + a >= 0) and (x + b >=0):
                            self.field[y+a][x+b]+=1
                    except:
                        pass
    
    def endGame(self):
        os.system('cls')
        for i in range(self.size):
            for j in range(self.size):
                if self.field[j][i] == '¤':
                    self.fieldVisible[j][i] = self.field[j][i]
                print(self.fieldVisible[i][j], end = ' ')
            print()
        print("You Lose")
        input()
        exit(0)

    def StartGame(self):
        self.fieldVisible = []
        for i in range(self.size):
            self.fieldVisible.append(['■']*self.size)

    def PrintField(self):
        input()
        os.system('cls||clear')
        for i in range(self.size):
            for j in range(self.size):
                print(self.fieldVisible[i][j], end = ' ')
            print()

    def PrintFieldGod(self):
        os.system('cls||clear')
        print()
        for i in range(self.size):
            for j in range(self.size):
                print(self.fieldVisible[i][j], end = ' ')
            print("", end = " :  ")
            for j in range(self.size):
                print(self.field[i][j], end = ' ')
            print()

    def OpenField(self, z):
        [y, x] = z
        if (self.field[y][x] != '¤'):
            self.fieldVisible[y][x] = self.field[y][x]
            if self.field[y][x] != 0: 
                return
            if self.field[y][x] == 0:
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if y + a >= 0 and x + b >= 0 and y + a < self.size and x + b < self.size:
                            if self.fieldVisible[y + a][x + b] != self.field[y + a][x + b]:
                                self.OpenField([y + a, x + b])
        else: 
            self.endGame()

    def Flag(self):
        pass

def main():        
    size = 20
    bomb = 20
    game = Game(size, bomb)
    game.StartGame()
    game.PrintFieldGod()
    z = [int(x) for x in input().split(" ")]
    game.OpenField(z)
    game.PrintFieldGod()
    input()

if __name__ == "__main__":
    main()