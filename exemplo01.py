#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *

fluxo=stream.Stream()


mao_esquerda=stream.PartStaff()
mao_direita=stream.PartStaff()

N=note.Note('C#5', type='quarter')
NDim=N.transpose('diminished5')
celZ=chord.Chord(['C2', 'E-2', 'F#2', 'A2'])
celZ.duration=duration.Duration(2.0)

ZDim=celZ.transpose('diminished5')

mao_esquerda.insert(0,clef.BassClef())
mao_esquerda.insert(1,meter.TimeSignature('5/4'))
mao_esquerda.insert(2,celZ)
mao_esquerda.insert(3,note.Rest())
mao_esquerda.insert(4,ZDim)

mao_direita.insert(0,clef.TrebleClef())
mao_direita.insert(1,meter.TimeSignature('5/4'))
mao_direita.insert(2,note.Rest())
mao_direita.insert(3,N)
mao_direita.insert(4,NDim)
mao_direita.insert(5,note.Rest())
mao_direita.insert(6,chord.Chord(['F#5','C6']))





#staffgrupo = layout.StaffGroup([mao_esquerda, mao_direita], name='Piano', abbreviation='Piano.', symbol='brace')
#staffgrupo.barTogether = 'yes'



fluxo.insert(0,mao_direita)
fluxo.insert(0,mao_esquerda)

fluxo.show('midi')
fluxo.show('lily.pdf')
