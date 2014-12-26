#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *
import os
import sys

localcorpus=os.getcwd()+'/localcorpus/'
localXML='mikro'+str(sys.argv[1])+'.xml'

localfile=localcorpus+localXML

MIKRO=converter.parse(localfile) 

#maodir=MIKRO.parts[0]
#maoesq=MIKRO.parts[1]
MIKROch=MIKRO.chordify()


sortedRhythms = search.mostCommonMeasureRythms(MIKROch)


vezes=[]
for s in sortedRhythms:
	vezes.append(s['number'])

comum=stream.Stream()
raro=stream.Stream()

for s in sortedRhythms:
	if (s['number']) == max(vezes):
		for m in s['measures']:
			comum.append(m)

for s in sortedRhythms:
	if (s['number']) == min(vezes):
		for m in s['measures']:
			raro.append(m)


if sys.argv[2] == 'comum':
	comum.show('lily.pdf')
else:
	if sys.argv[2] == 'raro':
		raro.show('lily.pdf')
	else:
		MIKROch.show('lily.pdf')


