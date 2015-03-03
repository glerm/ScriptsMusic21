#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *
import os
import sys

localcorpus=os.getcwd()+'/localcorpus/'
localXML='mikro'+str(sys.argv[1])+'.xml'

localfile=localcorpus+localXML

MIKRO=converter.parse(localfile) 

maodir=MIKRO.parts[0]
maoesq=MIKRO.parts[1]

#nota inicial mao esquerda 
IniE=note.Note(str(sys.argv[2]))
nota_inicial_ESQ=IniE.midi
#nota inicial mao direita 
IniD=note.Note(str(sys.argv[3]))
nota_inicial_DIR=IniD.midi


#NCR = nota code or rest
for NCR in maoesq.flat.notes:
	if NCR.isNote:
		contorno_atual=NCR.midi-nota_inicial_ESQ
		nota_inicial_ESQ=NCR.midi
		NCR.addLyric(NCR.name)
		NCR.addLyric(contorno_atual)
	if NCR.isChord:
		NCR.addLyric(NCR.forteClassTn)


#NCR = nota code or rest
for NCR in maodir.flat.notes:
	if NCR.isNote:
		contorno_atual=NCR.midi-nota_inicial_DIR
		nota_inicial_DIR=NCR.midi
		NCR.addLyric(NCR.name)
		NCR.addLyric(contorno_atual)
	if NCR.isChord:
		NCR.addLyric(NCR.forteClassTn)





MIKRO.show('lily.pdf')
