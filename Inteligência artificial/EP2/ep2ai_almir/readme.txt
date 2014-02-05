Almir Alves Pereira 6431238

MAC0425 - Inteligência Artificial - Segundo EP - MDP e iteração de valor

Para rodar o ep inicie o interpretador python e digite:
from parser import *
Para carregar mapas:
parser("nome do arquivo")
Ou para usar o arquivo padrão:
parser()

Os arquivos de mapa devem seguir o mesmo padrão dos arquivos map1 e map2 fornecidos

Testes:
- Teste com o map1:
m = parser()
print_table(m.to_arrows(policy_iteration(m)))
Resultado:
>   >      >   >   >
>   >      >   ^   .
>   None   >   >   .
>   >      >   >   ^
>   >      >   >   >

- Teste com o map2:
m = parser("map2")
print_table(m.to_arrows(policy_iteration(m)))
Resultado:
>   >      >   >   >
>   >      >   ^   .
>   None   >   ^   .
>   >      >   >   >
>   >      >   >   >

- Teste com o map3:
m = parser("map3")
print_table(m.to_arrows(policy_iteration(m)))
Resultado:
>   >      >   >   >
>   >      >   ^   .
>   None   >   <   .
>   >      >   >   v
>   >      >   >   >

Nota: Apesar do professor ter dito para usar gamma = 1, usei gamma = 0.9, pois quando usei 1 o algoritmo de iteração de valor enrou em loop infinito