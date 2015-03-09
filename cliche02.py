#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *
import random

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
		nota=note.Note('C5',quarterLength=d)
	else:	
		if d[1] == 'I1':
			nota=note.Note('C5',quarterLength=d[0])
			s=[nota]
			I1=nota		
	
		if d[1] == 'F1':
			nota=note.Note('C5',quarterLength=d[0])
			l=[I1,nota]	
			ligado = spanner.Slur(l)
			m.insert(0,ligado)

		if d[1] == 'I2':
			nota=note.Note('C5',quarterLength=d[0])
			s=[nota]
			I2=nota		
	
		if d[1] == 'F2':
			nota=note.Note('C5',quarterLength=d[0])
			l=[I2,nota]	
			ligado = spanner.Slur(l)
			m.insert(0,ligado)
	

	m.append(nota)



print notas
m.show('musicxml')
