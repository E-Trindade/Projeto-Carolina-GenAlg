from Tela import *
from Entidades import Criatura, Vetor
from random import randint, random
from pprint import pprint
#import numpy as np
#Constantes
TAMANHO_GERACAO = 50
CROSSOVER_RATE = 0.7 # ???? Not used
TAXA_MUTACAO = 0.002
'''
Exemplo de genoma
00110011001110 (bin)
_______ _______
Vel		ang
'''
def testar(genoma):
	criatura = conjurar( Criatura(genoma = genoma) )

	alvoX = ALVO[0] + 2.5	
	dist = abs(criatura.x - alvoX)	

	return criatura.aptidao, dist
def sortear(valores):#Sorteia um item de um dicionario com base no peso de suas chaves (Método da roleta de cassino)
	soma = sum(valores.values())
	somaRelativa = 0
	for chave, peso in valores.items():
		somaRelativa += peso / soma #Calcula a porcao da roleta que esse item representa
		numSort = random()
		if numSort <= somaRelativa:
			return chave

#O ciclo da vida
#Lista mae
#Gera umas lista de (TAMANHO_GERACAO) genomas aleatórios
genomas_base = ['%014d' %int(bin(randint(0,16384))[2:]) for i in range(0, TAMANHO_GERACAO)] #TODO: Garantir que não existam dois genomas iguais nessa lista
geracao = genomas_base
pprint('Geração 0:')
pprint(geracao)

contador_geracoes = 0
while True: # Gera uma nova geração
	individuos = {}
	distancias = []
	#Testando toda a geracao e gerando lista de aptidao
	for genoma in geracao:
		apt,dist = testar(genoma)
		individuos[genoma] = apt
		distancias.append(dist)
	novaGeracao = [] 
	#Populando a nova geracao
	while len(novaGeracao) <= TAMANHO_GERACAO:
		#Sorteando 2 organismos
		org1 = sortear(individuos)
		org2 = sortear(individuos)
		#cont = 0
		#while org2 == org1 or cont < 5:
		org2 = sortear(individuos)
			#cont +=1
		#print('Organismos escolhidos: \n%s\n%s' %(org1,org2))
		#Reproduzindo os dois

		#Crossover
		filho = ''
		indice_heranca = randint(0,14)
		filho = org1[:indice_heranca] + org2[indice_heranca:]
		#Mutacao
		mut = ''
		for val in filho:
			if random() < TAXA_MUTACAO:
				mut += '1' if val == '0' else '0'
			else:
				mut += val
		filho = mut
		#Adiciona o filho à nova geracao
		#if filho not in novaGeracao:
		novaGeracao.append(filho)
		#print(novaGeracao)
	geracao = novaGeracao
	contador_geracoes += 1
	
	#Imprime na tela a nova geracao
	#pprint('Média de distância da geração: %f' %np.mean(distancias))

	pprint('Geração %d:' %contador_geracoes)
	pprint(geracao)
	

