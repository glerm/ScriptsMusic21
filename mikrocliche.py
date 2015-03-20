#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *
from random import *
from copy import *


####################### teste da biblioteca de cliches mikrokosmos
from clichelib import *
from sys import argv

escala=argv[1]
tom=argv[2]
inicio=argv[3]
fim=argv[4]


# dados para teste
# 1. duracoes com ligados
durs1=[1.0,[1.0,'I'],[1.0,'F'],2.0,1.0]
durs2=[1.0,1.0,[2.0,'I'],[1.5,'F'],1.5]
durs3=[2.0, 1.0, 2.0,1.0]


# 2. uma celula base a partir das escalas
motivo=escalachoice(escala,tom,inicio,fim)


# inicia um cliche vazio
cliche=stream.Stream()

# variavel de inicio 
Linicio=0

# loop para o sorteio de 8 compassos
for x in xrange(32):
	#sorteia um dos dois motivos
	c=choice([durs1,durs2,durs3])

	#chama a funcao que cria os cliches a partir da lista de ritmos e notas
	s=clichelize(c,motivo)
	
	#insere os cliches
	for i in s:
		cliche.append(deepcopy(i))

	# insere pausa no final do motivo
	cliche.append(note.Rest())	
	
	# insercao da ligadura baseada na primeira e ultima nota do motivo atual
	l=[cliche[Linicio],cliche[len(cliche)-2]]
	ligado = spanner.Slur(l)
	cliche.insert(Linicio,ligado)
	Linicio=(len(cliche))
	
	
#formatacao de uma metrica padrao para insercao, fazendo os motivos ajustarem
cliche.makeMeasures(meterStream=meter.TimeSignature('6/4') , inPlace=True)
	

#vexflow.fromScore(cliche, mode='txt')
#cliche.show('text') # conferencia da estrutura de dados
cliche.show('musicxml') # o ligado de expressao so aparece no musicxml
