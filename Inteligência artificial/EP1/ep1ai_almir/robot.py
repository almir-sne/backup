# -*- coding: latin-1 -*-

from state import *
from copy import copy

# A classe robot representa um robo
# state_map representa o mapa interno do robo, que é construido conforme ele anda
# start é a posição inicial
# position é a posição atual do robo
# goal é o objetivo
# open_list guarda os estados que estão com t = OPEN
class robot():
    # Na inicialização, a classe recebe o ponto de partida e o ponto de chegada e
    # cria a configuração inicial dos backpointers 
    def __init__ (self, px, py, gx, gy):
        self.goal = point (gx, gy)
        self.start = point (px, py)
        self.position = point (px, py)
        self.state_map = self.state_matrix ()
        self.open_list = state_list ()
        self.open_list.insert(self.state_map[gx][gy], 0)
        while self.state_map[px][py].t != CLOSED and self.process_state() != -1:
            pass
        print "Robot says:  YOU CAN'T ESCAPE HUMANOID!"

    # Recebe o mapa do ambiente e imprime a trajetória do robo na saída padrão
    def print_map (self, map):
        print " y"
        print " v 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 <- x"
        for j in range(0, 18):
            print str(j).rjust(2),
            for i in range(0, 18):
                if map[i][j] == EMPTY:
                    if point (i, j) == self.goal:
                        print 'G',
                    elif point (i, j) == self.start:
                        print 'S',
                    elif self.state_map[i][j].path == 1:
                        print 'R',
                    else:
                        print ' ',
                else:
                    print 'O',
            print ('\n'),
        print " ^ 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 <- x"
        print " y"
        print "Legenda:\n G -> objetivo\n S -> ponto de partida\n O -> obstaculo\n R -> local por onde o robo passou"

    # Recebe o mapa do ambiente e move o robo em 1 posição
    # Se houver uma discrepancia entre o mapa do robo e o ambiente,
    # atualiza o mapa e os backpointers
    # Devolve 1 se o robo chegou no objetivo e 0 caso contrario
    def move (self, map):
        if self.position == self.goal:
            return 1
        p = point (self.position.x, self.position.y)
        x = self.state_map[p.x][p.y]
        if map[x.backpointer.x][x.backpointer.y] == OBSTACLE:
            h = x.h
            self.modify_cost (x.backpointer, OBSTACLE)
            kmin = -2
            while kmin < h and kmin != -1:
                kmin = self.process_state()
        else:
            self.state_map[p.x][p.y].path = 1
            self.position.x = x.backpointer.x
            self.position.y = x.backpointer.y
        return 0

    # Recebe um estado y e seu novo custo cval
    # Atualiza o custo de y e o insere na lista de estados abertos
    # Devolve o estado da lista com menor k
    def modify_cost (self, y, cval):
        y.c = cval
        if y.t == CLOSED:
            self.open_list.insert (y, y.h)
        return self.open_list.get_kmin ()

    # Recebe dois inteiros i e j, ambos entre 0 e 17
    # Devolve uma lista contendo todos os estados vizinhos de state_map[i][j]
    def get_neighbors(self, i, j):
        neighbors = []
        if i > 0 and j < 17:
            neighbors += [self.state_map[i - 1][j + 1]]
        if i < 17 and j > 0:
            neighbors += [self.state_map[i + 1][j - 1]]
        if i < 17 and j < 17:
            neighbors += [self.state_map[i + 1][j + 1]]
        if i > 0 and j > 0:
            neighbors += [self.state_map[i - 1][j - 1]]
        if i > 0:
            neighbors += [self.state_map[i - 1][j]]
        if i < 17:
            neighbors += [self.state_map[i + 1][j]]
        if j > 0:
            neighbors += [self.state_map[i][j - 1]]
        if j < 17:
            neighbors += [self.state_map[i][j + 1]]
        return neighbors

    # Atualiza os backpointers dos estados
    # Devolve o menor valor de k da lista de estados abertos
    def process_state (self):
        x = self.open_list.delete()
        if x == None:
            return -1
        kold = x.k
        neighbors = self.get_neighbors(x.x, x.y)
        if kold < x.h:
            for y in neighbors:
                if y.h != None and y.h <= kold and x.h > y.h + y.c:
                    x.backpointer = y
                    x.h = y.h + y.c
        if kold == x.h:
            for y in neighbors:
                if (y.t == NEW or ((y.backpointer is x) and (y.h != x.h + x.c)) or
                (y.backpointer is not x and y.h > x.h + x.c)):
                    y.backpointer = x
                    self.open_list.insert(y, x.h + x.c)
        else:
            for y in neighbors:
                if y.t == NEW or (y.backpointer is x and y.h != x.h + x.c):
                    y.backpointer = x
                    self.open_list.insert(y, x.h + x.c)
                elif y.backpointer is not x and y.h > x.h + x.c:
                    self.open_list.insert(x, x.h)
                elif (y.backpointer is not x and x.h > y.h + y.c and y.t == CLOSED
                and y.h > kold):
                    self.open_list.insert(y, y.h)
        return self.open_list.get_kmin()

    # Usando as tecnicas mais avancadas de POG, cria uma matriz de estados
    # As bordas da matriz já são inicializadas como obstaculos
    # Devolve a matriz criada
    def state_matrix (self):
        mat = []
        for i in range(0, 18):
            x = []
            for j in range(0, 18):
                x += [state(i, j)]
            mat += [x]
        for i in range(0, 18):
            mat[0][i].c = mat[i][0].c = mat[17][i].c = mat[i][17].c = OBSTACLE
        return mat
