#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *

# Criamos um objeto score (partitura) para usar como fluxo
partitura=stream.Score()

# Separamos o fluxo em duas partes: duas pautas
mao_esquerda=stream.PartStaff()
mao_direita=stream.PartStaff()

# Criamos os compassos para cada pauta 
compasso1L=stream.Measure(number=1)
compasso1R=stream.Measure(number=1)

# Necessitamos formatar o layout do score para agrupar as duas pautas
compasso1L.insert(0,layout.SystemLayout())
compasso1L.insert(0,layout.StaffLayout(staffNumber=2))

# Inserindo a clave, a formula de compasso, nota e acorde
compasso1L.insert(0,clef.BassClef())
compasso1L.insert(0,meter.TimeSignature('2/4'))
compasso1L.insert(0,note.Note('F3'))
compasso1L.insert(1,chord.Chord(['A2','E3','C4']))

# Inserindo o compasso da pauta da mao esquerda na parte inferior
mao_esquerda.insert(0,compasso1L)

# Inserindo a clave, a formula de compasso, nota e pausa
compasso1R.insert(0,layout.SystemLayout())
compasso1R.insert(0,clef.TrebleClef())
compasso1R.insert(0,meter.TimeSignature('2/4'))
compasso1R.insert(0,note.Note('C5'))
compasso1R.insert(1,note.Rest())

# Inserindo o compasso da pauta da mao direita na parte superior
mao_direita.insert(0,compasso1R)

# Formatando a entrada das partes na camada de layout da partitura
partitura.insert(0,mao_direita)
partitura.insert(0,mao_esquerda)

# Renderizando em PDF
partitura.show('lily.pdf')
