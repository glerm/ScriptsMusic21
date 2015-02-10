#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *
import os
import sys

localcorpus=os.getcwd()+'/localcorpus/'
localXML='mikro'+str(sys.argv[1])+'.xml'

localfile=localcorpus+localXML

MIKRO=converter.parse(localfile) 

m=MIKRO.chordify()

for NCR in m.flat.notes:
	if NCR.isNote:
		contorno_atual=NCR.midi-nota_inicial_ESQ
		nota_inicial_ESQ=NCR.midi
		NCR.addLyric(NCR.name)
		NCR.addLyric(contorno_atual)
	if NCR.isChord:
		NCR.addLyric(NCR.forteClassTn)


m.show('lily.pdf')
