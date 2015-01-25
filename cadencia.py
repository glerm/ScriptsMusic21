#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *

k=['iii6','V7','I64', 'V7']
#k=['I6','ii','IV','V7','I']
T='C' 

s=stream.Stream()

for i in k:
	n=roman.RomanNumeral(str(i),T)
	c=chord.Chord(n.pitches)
	c.addLyric(str(i))
	s.append(c) 

fim=chord.Chord(['C4','G4','C5','E5','C6'])
fim.addLyric('I')

s.append(fim)
 

s.show('midi')
s.show('lily.pdf')
