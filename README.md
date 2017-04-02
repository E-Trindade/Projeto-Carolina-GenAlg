# Projeto-Carolina - Algoritmo Genético
Projeto de algoritmo genético feito em Python (+ um mini motor de física)

* Requer Pygame

A princípio, é gerada uma lista de indivíduos, cada qual com seu genoma, em binário. Cada criatura tem o seu código genético como o ângulo e a força com que pode saltar. Baseando-se na distância final do salto em relação ao alvo, é gerada uma pontuação de aptidão para o indivíduo. <br>
Finalmente, após todos terem sido testados, é usado o método de *Roulette-wheel selection* para cruzar os genomas (Genomas mais aptos têm mais chance de procriar). Nessa etapa, também podem ocorrer mutações nos genomas filhos.
Em seguida, a nova geração é testada, repetindo o ciclo.

## Notas
Com o tempo, percebi que:
- Aumentando o número de indivíduos por geração, há uma maior "competição" entre os indivíduos, levando a uma variedade maior de genótipos e, consequentemente, uma aproximação melhor dos saltos de alguns em relação ao alvo.
- Em contrapartida, com um tamanho de geração baixo, a tendência é que as gerações descendentes se miscigenem e todos os seres tenham o mesmo código genético (!), geralmente apresentando uma baixa aptidão geral. (A única coisa que pode impedir isso é uma taxa de mutação média-elevada)

Esse projeto foi feito como hobby, apenas por curiosidade em relação a alguns tópicos de IA, enquanto eu ainda estava no técnico (lá por meados de 2014).

Meu objetivo no futuro é passar esse projeto (Principalmente o motor de física baseado em vetores) para Javascript, usando o Canvas do HTML5, já que o Pygame não é uma das bibliotecas mais portáteis.
