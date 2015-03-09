#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *
import random

m=stream.Stream()
metrica='2/4'


durs=[[1.0,'I',1],1.0,1.0,1.0,2.0,1.0,1.0,1.0,1.0,[1.0,'F',1]]
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
		if d[1] == 'I':
			nota=note.Note('C5',quarterLength=d[0])
			s=[nota]
			nota_inicio=nota		
	
		if d[1] == 'F':
			nota=note.Note('C5',quarterLength=d[0])
			l=[nota_inicio,nota]	
			ligado = spanner.Slur(l)
			m.insert(0,ligado)
	

	m.append(nota)



print notas
m.show('musicxml')
