#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *
from random import *
from copy import *



durs1=[1.0,1.0,1.0,1.0,[2.0,'I'],[1.0,'F'],1.0,1.0,1.0,1.0,'F1']
durs2=[1.0,0.5,[0.5,'I'],[1.0,'F'],0.5,0.5]


def clichelize(durations):
		cliche=stream.Stream()
		for d in durations:
			if type(d) is float:	
				nota=note.Note('C5',quarterLength=d)
			else:	
				#beam ligadura de continuacao
				if d[1] == 'I':
					nota=note.Note('C5',quarterLength=d[0])
					nota.tie=tie.Tie("start")
				
				if d[1] == 'F':
					nota=note.Note('C5',quarterLength=d[0])
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
for x in xrange(8):
	c=choice([durs1,durs2])
	s=clichelize(c)
	for i in s:
		cliche.append(deepcopy(i))
	cliche.append(note.Rest())	

cliche.makeMeasures(meterStream=meter.TimeSignature('2/4') , inPlace=True)
	



cliche.show('lily.pdf')
