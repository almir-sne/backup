 - Arquivos:
map* -> arquivos de mapas
interface.py -> lê dados do usuário e lê o arquivo de mapa (ambiente)
robot.py -> contém a classe que representa o robô (agente inteligente)
state.py -> contém a classe que representa os estados do robô e a classe que representa a lista de estados abertos

 - Os mapas que o algoritmo lê têm a seguinte forma:
OOOOOOOOOOOOOOOOOO
O                O
O                O
O                O
O                O
O                O
O                O
O                O
O                O
O                O
O                O
O                O
O                O
O                O
O                O
O                O
O                O
OOOOOOOOOOOOOOOOOO
O -> obstaculo
espaço -> celula vazia

 - O mapa tem 16x16 celulas, mas é representado com 18x18 celulas. As celulas extras são para representar as bordas do mapa.

 - O robô pode andar em 8 direções. Cada direção tem o mesmo custo o que pode causar um comportamento estranho: o robô andar em zigue-zague até o objetivo ao invés de andar em linha reta, pois o custo do caminho em zigue-zague é o mesmo do caminho em linha reta.

 - Para executar o programa abra o seu emulador de terminal favorito e digite:
python interface.py

 - O programa assume que o problema sempre tem solução, se não tiver pode entrar em loop infinito

 - Dados para testar:
map1, partida: (16, 16) chegada: (1, 16)
map2, partida: (10, 7) chegada: (10, 9)
map3, partida: (1, 16) chegada: (1, 1) -> este é o pior caso do algoritmo, o robô anda por todo o mapa
map4, partida: (1, 16) chegada: (16, 1)