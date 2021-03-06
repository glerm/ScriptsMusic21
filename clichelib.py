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



########## escalas

def escalachoice(escala,tom,inicio,fim):
	if escala == 'penta':

		pitchList = ["C4","D4","F4","G4","A4"]
		PentaScale = scale.AbstractScale()
		PentaScale.buildNetworkFromPitches([pitch.Pitch(p) for p in pitchList])
		e = PentaScale._net.realizePitch(tom)

	if escala == 'tonsint':

		pitchList = ["C4","D4","E4","F#4","G#4","A#4","C5"]
		WT = scale.AbstractScale()
		WT.buildNetworkFromPitches([pitch.Pitch(p) for p in pitchList])
		e = WT._net.realizePitch(tom)


	if escala == ('maior' or 'jonio'):
		Maior = scale.MajorScale(tom)
		e = Maior.getPitches()


	if escala == 'dorico':
		Dorian = scale.DorianScale(tom)
		e = Dorian.getPitches()


	if escala == 'frigio':
		Frigio = scale.PhrygianScale(tom)
		e = Frigio.getPitches()

	if escala == 'lidio':
		Lidio = scale.LydianScale(tom)
		e = Lidio.getPitches()

	if escala == 'mixolidio':
		MLidio = scale.MixolydianScale(tom)
		e = MLidio.getPitches()

	if escala == ('menor' or 'eolio'):
		Menor = scale.MinorScale(tom)
		e = Menor.getPitches()

	if escala == 'locrio':
		Locrio = scale.LocrianScale(tom)
		e = Locrio.getPitches()

	if escala == 'octa':
		Octa = scale.OctatonicScale(tom)
		e = Octa.getPitches()



	return e[int(inicio):int(fim)]






