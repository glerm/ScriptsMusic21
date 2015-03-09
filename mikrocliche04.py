#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *
import random


n_compassos=16
metrica='2/4'

# Criamos um objeto score (partitura) para usar como fluxo principal
partitura=stream.Score()

# Separamos o fluxo em duas partes: duas pautas
mao_esquerda=stream.PartStaff()
mao_direita=stream.PartStaff()


#Criamos o primeiro compasso para cada pauta 
compasso1L=stream.Measure(number=1)
compasso1R=stream.Measure(number=1)

# Necessitamos formatar o layout do staff para agrupar as duas pautas
compasso1L.insert(0,layout.SystemLayout())
compasso1L.insert(0,layout.StaffLayout(staffNumber=2))
compasso1R.insert(0,layout.SystemLayout())

# Inserindo a clave, a formula de compasso inicial
compasso1L.insert(0,clef.BassClef())
compasso1L.insert(0,meter.TimeSignature(metrica))
mao_esquerda.insert(0,compasso1L)

# Inserindo a clave, a formula de compasso inicial
compasso1R.insert(0,clef.TrebleClef())
compasso1R.insert(0,meter.TimeSignature(metrica))
mao_direita.insert(0,compasso1R)


########## escalas

pitchList = ["C4","D4","F4","G4","A4","C5"]
PentaScale = scale.AbstractScale()
PentaScale.buildNetworkFromPitches([pitch.Pitch(p) for p in pitchList])
escala_melodia = PentaScale._net.realizePitch('D5')

escala2 = scale.DorianScale('D')
escala_baixo=escala2.getPitches('d2', 'd3')
TAM_linha_baixo=len(escala_baixo)


random.shuffle(escala_baixo)
escala_melodia.reverse()
###################################


for n in xrange(n_compassos):	
	compasso_esquerdo=stream.Measure(number=n)
	compasso_direito=stream.Measure(number=n)

	for t in xrange(8):
		baixo=note.Note(escala_baixo[(rotacao1+t)%TAM_linha_baixo],
		quarterLength=.5)
		compasso_esquerdo.append(baixo)
		
		melodia=note.Note(escala_melodia[(rotacao2+t)%6],
		quarterLength=.5)
		compasso_direito.append(melodia)

	

	mao_esquerda.insert(n,compasso_esquerdo)
	mao_direita.insert(n,compasso_direito)


# Formatando a entrada das partes na camada de layout da partitura
partitura.insert(0,mao_direita)
partitura.insert(0,mao_esquerda)




##################### processamento
P='lily.pdf'
M='midi'
T='text'
X='musicxml'

partitura.show(X)

