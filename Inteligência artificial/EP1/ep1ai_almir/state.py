# -*- coding: latin-1 -*-

from heapq import *

[NEW, OPEN, CLOSED] = range(0, 3)
EMPTY = 1
OBSTACLE = 314

# Um simples ponto (x, y) com relação de igualdade definida
class point():
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __eq__ (self, other):
        return (self.x == other.x and self.y == other.y)

# A classe state define um estado do mapa interno do robo
# t é uma tag e pode ter os valores NEW, OPEN e CLOSED
# c indica se o estado é vazio ou obstaculo
# backpointer indica qual o proximo estado que deve ser seguido
# h é o custo para chegar até o objetivo
# k é o menor custo que h assumiu desde que entrou na lista de estados abertos
# path é uma flag que indica que o robo passou por este estado
# x e y representam a posição do estado
class state():
    def __init__ (self, x, y):
        self.t = NEW
        self.c = EMPTY
        self.backpointer = None
        self.h = None
        self.k = None
        self.path = None
        self.x = x
        self.y = y

    # Define a relação de igualdade entre estados, que são comparados usando o k
    def __eq__ (self, other):
        if other == None:
            return False
        return self.k == other.k

    # Define a relação de desigualdade entre estados
    def __ne__ (self, other):
        if other == None:
            return True
        return self.k != other.k

    # Define a comparação entre estados para ser usada com a biblioteca heapq
    # Devolve um numero negativo se self.k < other.k, zero se self.k < other.k e
    # um numero positivo se self.k > other.k
    def __cmp__ (self, other):
        return self.k - other.k

# Classe que representa a lista de estados abertos, implementada usando a biblioteca heapq
# O heap é ordenado usando o k dos estados
class state_list ():
    def __init__ (self):
        self.heap = []

    # Recebe um estado x e seu novo h, hnew
    # Atualiza o k e o h de x e o insere na lista
    def insert (self, x, hnew):
        if x.t == NEW:
            x.k = hnew
        elif x.t == OPEN:
            # Neste caso x precisa ser removido, atualizado e inserido novamente no heap
            if hnew < x.k:
                for i in range (0, len(self.heap)):
                    if self.heap[i] is x:
                        self.heap.pop(i)
                        heapify(self.heap)
                        break
                x.k = hnew
        else:
            if hnew < x.h:
                x.k = hnew
            else:
                x.k = x.h
        x.h = hnew
        x.t = OPEN
        heappush(self.heap, x)

    # Devolve o menor valor de k da lista
    def get_kmin(self):
        if self.heap == []:
            return -1
        return self.heap[0].k

    # Remove o estado que tem o menor k do heap
    # Devolve estado x com o menor valor de k
    def delete(self):
        if self.heap == []:
            return None
        x = heappop(self.heap)
        x.t = CLOSED
        return x