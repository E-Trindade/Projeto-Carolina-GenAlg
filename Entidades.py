nomes = ['Cláudio','Josefina','Lúcio','Maria Clara','Josifredo','Petúnia','Ricardo','Rosefrilde','Poroshenko','Lucashenko','Pudjin']
import random,math
def rad(x):
	return math.radians(x)
def distancia(p1,p2):
	x1,y1 = p1
	x2,y2 = p2
	px = max(x1,x2) - min(x1,x2)

	py = max(y1,y2) - min(y1,y2)
	dist = math.sqrt(px**2 + py**2)
	return dist
	
#Fisica, bitches
#Todo: Passar logica de vetores e coord pra ca
class Vetor(object):
	def __init__(self, forca, ang=None, angRad=None):
		self.forca = forca
		if angRad is not None:
			self.ang = angRad
		else:
			self.ang = rad(ang)
	def __repr__(self):
		return '<Vetor: Forca: %f, Angulo: %f>' %(self.forca,self.ang)
#Operacoes com vetores
def normalizarVetor(vet):
	#if vet.forca < 0:#Se o modulo for menor que 0, troca o sentido do vetor
	#	vet.ang += 180
	#	vet.forca *= -1
	#if vet.ang < 0:
	#	while vet.ang < 0:
	#		vet.ang += rad(360)
	#elif vet.ang >= rad(360):
	#	while vet.ang >= rad(360):
	#		vet.ang -= rad(360)
	return vet
def somarVetores(v1, v2):
	#print(v1,v2)
	if v1 is None: return v2
	if v2 is None: return v1
	x = math.cos(v1.ang) * v1.forca + math.cos(v2.ang) * v2.forca
	y = math.sin(v1.ang) * v1.forca + math.sin(v2.ang) * v2.forca
	#print(x,y)
	forcaRes = math.hypot(x,y)
	angRes = math.pi/2 - math.atan2(x,y)
	#print(angRes)
	#print(forcaRes,angRes)
	rt = Vetor(forcaRes, angRad = angRes) 

	return normalizarVetor(rt)

class objeto_fisico(object):
	def __init__(self,x = 0,y = 0, velocidade = None, aceleracao = None):
		self.x = x
		self.y = y
		self.velocidade = velocidade
		self.aceleracao = aceleracao
	def adicionarAceleracao(self,acel):
		self.aceleracao = somarVetores(self.aceleracao, acel)
	def mover(self,t):
		#Movendo o objeto
		vx,vy = math.cos(self.velocidade.ang) * self.velocidade.forca, math.sin(self.velocidade.ang) * self.velocidade.forca
		self.x = self.x + vx * t
		self.y = self.y + vy * t
		#Aplicando a aceleracao
		if self.aceleracao is not None:
			ax,ay = math.cos(self.aceleracao.ang) * self.aceleracao.forca, math.sin(self.aceleracao.ang) * self.aceleracao.forca
			vx2 = vx + ax * t
			vy2 = vy + ay * t
			vetorV = somarVetores(Vetor(vx2,0), Vetor(vy2,90))
			#print(vetorV)
			self.velocidade = vetorV
class Criatura(objeto_fisico):
	aptidao = None
	genoma = None
	def decodificar(self,genoma):
		vel = int(genoma[:8],2)
		ang = int(genoma[8:],2)
		if ang > 90: ang = 90
		if vel > 100: vel = 100
		self.velocidade = Vetor(vel,ang)
	def __init__(self,x = 0,y = 0, velocidade = None, aceleracao = None, genoma = None):
		#Atributos fisicos
		self.genoma = genoma
		self.x = x
		self.y = y
		self.aceleracao = aceleracao
		if genoma is not None:
			self.decodificar(genoma)
		else:
			self.velocidade = velocidade

		self.nome = random.choice(nomes)
		print(self.nome , 'nasceu!')
	def __repr__(self):
		retorno = '<Criatura - Nome: %s, Genoma: %s, Velocidade: %s, X: %.3f, Y:%.3f >' %(self.nome,self.genoma,self.velocidade,self.x,self.y)
		return retorno