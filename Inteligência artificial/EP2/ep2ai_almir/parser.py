# -*- coding: latin-1 -*-
import re
from mdp import *

# Recebe um nome de arquivo
# Processa o mapa contido no arquivo
# Devolve um GridMDP que representa o mapa contido no arquivo
def parser (map_name = "map1"):
    # Definição de expresões regulares
    read_float = re.compile("([-+]?\d+(\.\d+)?)|(None)")

    # Processamento do arquivo de mapa
    map = open (map_name, 'r')
    result = re.match("Tamanho: (\d+)x(\d+)", map.readline())
    size_x = int(result.groups()[0])
    size_y = int(result.groups()[1])
    map_mat = []
    for i in range(0, size_y):
        result = read_float.findall(map.readline())
        x = []
        for j in range(0, size_x):
            if result[j][2] == 'None':
                x += [None]
            else:
                x += [float(result[j][0])]
        map_mat += [x]

    begin = re.match("Inicio: (\d+),(\d+)", map.readline())
    init = (int(begin.groups()[0]), int(begin.groups()[1]))

    obj = re.match("Objetivo: (\d+),(\d+)", map.readline())
    forb = re.match("Proibido: (\d+),(\d+)", map.readline())
    terminals = [(int(obj.groups()[0]), int(obj.groups()[1])), (int(forb.groups()[0]), int(forb.groups()[1]))]


    north = re.match("Norte: [-+]?(\d+(\.\d*)?|\.\d+)", map.readline())
    south = re.match("Sul: [-+]?(\d+(\.\d*)?|\.\d+)", map.readline())
    east = re.match("Leste: [-+]?(\d+(\.\d*)?|\.\d+)", map.readline())
    west = re.match("Oeste: [-+]?(\d+(\.\d*)?|\.\d+)", map.readline())

    E = float(east.groups()[0])
    W = float(west.groups()[0])
    N = float(north.groups()[0])
    S = float(south.groups()[0])
    if N+S+E+W != 1:
        print "Erro! A soma das probabilidades de transição deve ser 1"
        exit()
    print ("Arquivo " + map_name + " carregado com sucesso (eu espero...)")
    return GridMDP (map_mat, terminals, N, S, W, E, init, 0.9)