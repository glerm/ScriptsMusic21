#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *
from random import *
from copy import *



def clichelize(durations,motivo):
		# a funcao vai formar um stream com as notas do motivo
		# posicionadas em cliches de segmentacao dolivro mikrokosmos 01
		cliche=stream.Stream()

		# para efeito de teste inserida uma funcao que sorteia notas para usar
		mesmo=choice(motivo)

		# para cada uma das duracoes inseridas na funcao
		for d in durations:

			# testa se o elemento tem nao tem ligadura
			if type(d) is float:	
				nota=note.Note(choice(motivo),quarterLength=d)

			# se tiver ligadura insere 
			else:	
				#beam: ligadura de continuacao
				# convencionamos I para o inicio da ligadura e F para o final
				if d[1] == 'I':
					nota=note.Note(mesmo,quarterLength=d[0])
					nota.tie=tie.Tie("start")
				
				if d[1] == 'F':
					nota=note.Note(mesmo,quarterLength=d[0])
					nota.tie=tie.Tie("stop")

			# faz uma copia da nota criada para usar no cliche
			cliche.append(deepcopy(nota))

		# retorna o cliche para a chamada da funcao
		return cliche


####################### teste da biblioteca de cliches mikrokosmos


# dados para teste
# 1. duracoes com ligados
durs1=[1.0,1.0,1.0, 2.0,1.0,1.0,1.0,1.0,1.0]
durs2=[1.0,1.0,1.0,2.0]

# 2. uma celula base de tres notas
motivo=['C4','D4','F4','G4','A4']

#motivo=['E-4','E4','B-4','B4']


# inicia um cliche vazio
cliche=stream.Stream()

# variavel de inicio 
Linicio=0

# loop para o sorteio de 16 compassos
for x in xrange(16):
	#sorteia um dos dois motivos
	c=choice([durs1,durs2])

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
cliche.makeMeasures(meterStream=meter.TimeSignature('3/4') , inPlace=True)
	


cliche.show('text') # conferencia da estrutura de dados
cliche.show('musicxml') # o ligado de expressao so aparece no musicxml
