#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *
from random import *
from copy import *
import sys





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


escala=sys.argv[1]
tom=sys.argv[2]
inicio=sys.argv[3]
fim=sys.argv[4]


#escala_melodia.reverse()

s= escalachoice(escala,tom,inicio,fim)



for n in s:
	print n




