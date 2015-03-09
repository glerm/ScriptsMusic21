#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *
from random import *

m=stream.Stream()
metrica='2/4'


durs=[[1.0,'I1'],1.0,1.0,1.0,[2.0,'I2'],[1.0,'F2'],1.0,1.0,1.0,[1.0,'F1']]
notas=len(durs)
divisor=1



## divisor
#for i in xrange(notas):
#	durs[i] = durs[i]/divisor


m.insert(0,clef.TrebleClef())
m.insert(0,meter.TimeSignature(metrica))


for d in durs:
	if type(d) is float:	
		nota=note.Note(choice(['B4','F#4','F4']),quarterLength=d)
	else:	

		# slur ligadura de expressao
		if d[1] == 'I1':
			nota=note.Note('C5',quarterLength=d[0])
			s=[nota]
			I1=nota		
	
		if d[1] == 'F1':
			nota=note.Note('C5',quarterLength=d[0])
			l=[I1,nota]	
			ligado = spanner.Slur(l)
			m.insert(0,ligado)


		#beam ligadura de continuacao
		if d[1] == 'I2':
			nota=note.Note('C5',quarterLength=d[0])
			nota.tie=tie.Tie("start")
	
	
		if d[1] == 'F2':
			nota=note.Note('C5',quarterLength=d[0])
			nota.tie=tie.Tie("stop")
	

	m.append(nota)

m.append(note.Rest())

m.makeMeasures(inPlace = True)
#m.makeRests(refStreamOrTimeRange=m[0], fillGaps=True, inPlace=True)





m.show('text')
m.show('musicxml')
