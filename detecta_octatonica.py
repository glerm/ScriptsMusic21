#!/usr/bin/env python
# -*- coding: utf-8 -*-

from music21 import *

# importa o arquivo mikrokosmos 109
localfile="localcorpus/mikro109.xml"

# converte para o formato music21
m=converter.parse(localfile)

# separa as duas partes
p0=m.parts[0]
p1=m.parts[1]

# cria uma escala de referencia octatonica
c=scale.OctatonicScale('C')


# verifica nota a nota (pulando acordes) se existem melodias dentro da escala
for n in p0.flat.notes:
	if n.isNote:
		n.addLyric(n.name)
		n.addLyric(str(c.getScaleDegreeFromPitch(n.pitch)))

for n in p1.flat.notes:
	if n.isNote:
		n.addLyric(n.name)
		if n.pitch.pitchClass == 8: #testa se há o Ab
			n.addLyric(str(c.getScaleDegreeFromPitch(n.pitch.getEnharmonic())))			
		else:			#se há o Ab troca para o G# no teste
			n.addLyric(str(c.getScaleDegreeFromPitch(n.pitch)))			
			
# imprime a partitura em pdf
m.show('lily.pdf')		




#n.name + " = " + str(c.getScaleDegreeFromPitch(n.nameWithOctave)))
