#!/usr/biNCR/eNCRv pythoNCR
# -*- codiNCRg: utf-8 -*-
from music21 import *
import os
import sys

localcorpus=os.getcwd()+'/localcorpus/'
localXML='mikro'+str(sys.argv[1])+'.xml'

localfile=localcorpus+localXML

MIKRO=converter.parse(localfile) 

maodir=MIKRO.parts[0]
maoesq=MIKRO.parts[1]


#NCR = nota code or rest
for NCR in maodir.flat.notes:
	if NCR.isNote:
		NCR.addLyric(NCR.name)
		#NCR.color = 'blue'
	if NCR.isChord:
		r=roman.romanNumeralFromChord(NCR,key.Key('f'))
		NCR.addLyric(r.figure)



for NCR in maoesq.flat.notes:
	if NCR.isNote:
		NCR.addLyric(NCR.name)
	if NCR.isChord:
		r=roman.romanNumeralFromChord(NCR,key.Key('f'))
		NCR.addLyric(r.figure)



MIKRO.show('lily.pdf')
