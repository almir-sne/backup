# -*- coding: latin-1 -*-

from robot import *
from state import *

# Recebe o nome do arquivo de mapa
# Devolve uma matriz de inteiros que representa o ambiente
def read_map (map_file="map1"):
    map = open(map_file)
    mat = []
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 18):
        mat += [copy(x)]
    j = 0
    for line in map:
        for i in range(0, 18):
            if line[i] == 'O':
                mat[i][j] = OBSTACLE
            else:
                mat[i][j] = EMPTY
        j += 1
    map.close()
    return mat

# Recebe as entradas do usuário e inicializa o robo
# Se o ponto de partida ou chegada for um obstaculo ou não existir,
# imprime uma mensagem de erro e termina o programa
map_name = raw_input ("Digite o nome do arquivo de mapa (pressione Enter para usar o padrao): ")
if map_name != '':
    map = read_map(map_name)
else:
    map = read_map()
px = input ("Digite o ponto de partida (x): ")
py = input ("Digite o ponto de partida (y): ")
gx = input ("Digite o ponto de destino (x): ")
gy = input ("Digite o ponto de destino (y): ")
if (px < 1 or px > 16 or py < 1 or py > 16 or gx < 1 or gx > 16 or gy < 1 or gy > 16
or map[px][py] == OBSTACLE or map[gx][gy] == OBSTACLE):
    print "Erro! Ponto de partida/chegada invalido"
    exit()
berzerk = robot(px, py, gx, gy)
# Movimenta o robo e imprime o mapa com a trajetoria
while berzerk.move(map) != 1:
    pass
berzerk.print_map(map)