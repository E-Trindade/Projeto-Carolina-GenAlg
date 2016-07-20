from pygame import *
from pygame.locals import *
from Entidades import Criatura, Vetor
import random, sys
import math
from pprint import pprint
#Cores
BLACK = (0 , 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (224, 224, 224)
COR_TRAJETORIA = (100,100,100)
#Fisica
DESENHAR_RAPIDO = False
TICK = 10
GRAVIDADE = Vetor(-10,90)
#Posicoes
WIDTH = 800
HEIGHT = 400
TEMPOINCREM = 0.1
ALVO = (WIDTH-100,HEIGHT-15,5,5) #Posicao do alvo: p(700,385) até p(705,390)
XINIT = 0
YINIT = 0

def iniciar():
	init()
	global DISPLAYSURF 
	DISPLAYSURF = display.set_mode((WIDTH,HEIGHT),0,32)
	DISPLAYSURF.fill(GRAY) # Fundo da tela
	display.set_caption('Lançamento oblíquo')
	desenharEixos()
	
def desenharEixos():
	draw.line(DISPLAYSURF,BLACK,(5,0),(5,600),5)# Eixo X
	draw.line(DISPLAYSURF,BLACK,(0,395),(800,395),5)# Eixo Y
	draw.rect(DISPLAYSURF,BLUE,((0,HEIGHT),(10,HEIGHT-10)),20)#Origem
	draw.rect(DISPLAYSURF,RED,ALVO,0)#Alvo

def desenhar(pontos,rapido = False):
	if DESENHAR_RAPIDO :
		#Quebrado
		if rapido: 
			pontosFormat = [(p[0] + 5 , HEIGHT - 5 - p[1]) for p in pontos]
			draw.lines(DISPLAYSURF,COR_TRAJETORIA,False,pontosFormat,1)
			event.pump()
		else:
			return
	else:
		if rapido:
			return
		else:
			pontosFormat = [(p[0] + 5 , HEIGHT - 5 - p[1]) for p in pontos]
			DISPLAYSURF.fill(GRAY)
			desenharEixos()
			draw.circle(
				DISPLAYSURF,
				GREEN,
				(
					int(pontosFormat[-1][0]),
					int(pontosFormat[-1][1])
				),5
			)
			#print((int(pontosFormat[:-1][0]),int(pontosFormat[:-1][1])))
			try:
				draw.lines(DISPLAYSURF,COR_TRAJETORIA,False,pontosFormat[:-1],3)
			except:
				pass
			finally:
				time.wait(TICK)
				display.update()
				event.pump()

def lancarVet(criatura):
	#Vetor = (vel,ang)
	posicoes = [(0,0)]
	criatura.aceleracao = GRAVIDADE
	t = 0
	while criatura.y > 0 or t == 0:
		desenhar(posicoes)
		
		criatura.mover(TEMPOINCREM)
		coord = (criatura.x,criatura.y)
		posicoes.append(coord)
		t += TEMPOINCREM
def conjurar(criatura):	
	iniciar()	
	lancarVet(criatura)	
	#Calculando aptidão	
	#Aptidao = 1/(distancia do alvo)	
	alvoX = ALVO[0] + 2.5	
	dist = abs(criatura.x - alvoX)	
	if dist == 0 :	
		criatura.aptidao = 0
	else:	
		criatura.aptidao = 1/(dist)	
	print('''Terminou de conjurar %s: 	
		X: %.3d,	
		Y: %.3d,
		Genoma: %s, 	
		Distancia: %.3f, 	
		Aptidao: %f''' %(criatura.nome,criatura.x, criatura.y,criatura.genoma, dist, criatura.aptidao))	
	return criatura	
	
	
	