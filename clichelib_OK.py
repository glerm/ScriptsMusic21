#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *
from random import *
from copy import *



durs1=[1.0,1.0,1.0,1.0,[2.0,'I'],[1.0,'F'],1.0,1.0,1.0,1.0,'F1']
durs2=[1.0,0.5,[0.5,'I'],[1.0,'F'],0.5,0.5]


def clichelize(durations,motivo):
		cliche=stream.Stream()
		mesmo=choice(motivo)
		for d in durations:
			if type(d) is float:	
				nota=note.Note(choice(motivo),quarterLength=d)
			else:	
				#beam ligadura de continuacao
				
				if d[1] == 'I':
					nota=note.Note(mesmo,quarterLength=d[0])
					nota.tie=tie.Tie("start")
				
				if d[1] == 'F':
					nota=note.Note(mesmo,quarterLength=d[0])
					nota.tie=tie.Tie("stop")
			cliche.append(deepcopy(nota))
		return cliche


#######################


'''
for b in xrange(8):
	s=stream.Stream()
	c=choice([durs1,durs2])
	cliche=deepcopy(clichelize(c))
	for n in cliche.flat.notes:
		print n
		s.append(n)
	l=[cliche[0],cliche[len(cliche)-1]]
	ligado = spanner.Slur(l)		
	s.insert(0,ligado)
'''
cliche=stream.Stream()
motivo=['A4','C5','F#5']
Linicio=0
for x in xrange(8):
	c=choice([durs1,durs2])
	s=clichelize(c,motivo)
	
	for i in s:
		cliche.append(deepcopy(i))



	cliche.append(note.Rest())	
	
	l=[cliche[Linicio],cliche[len(cliche)-2]]
	ligado = spanner.Slur(l)
	cliche.insert(Linicio,ligado)
	Linicio=(len(cliche))
	
	

cliche.makeMeasures(meterStream=meter.TimeSignature('2/4') , inPlace=True)
	


cliche.show('text') 
cliche.show('musicxml') # o ligado d eexpressao so aparece no musicxml
