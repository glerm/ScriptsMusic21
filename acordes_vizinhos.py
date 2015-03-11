#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *

#Script estudo sobre transformacoes por vizinhanca no ciclo das 3as maiores


# acorde de 5a aumentada
d = duration.Duration(4.0)
duration=d
c1=chord.Chord(['C4','E4','A-4'], duration=d)
c1.addLyric('C E Ab')
c1.addLyric(c1.commonName)
c1.addLyric(c1.normalFormString)	
c1.addLyric(c1.forteClassTn)
s=stream.Stream()
s.append(c1)
 
for n in xrange(len(c1)):
	### uma nota mais 1 semitom
	intervalo=interval.Interval(+1)
	t=c1[n].transpose(intervalo)
	c=chord.Chord([t,c1[((n+1)%3)],c1[((n+2)%3)]],duration=d)
	c.addLyric(c1[n].name+' mais 1 Semitom')
	c.addLyric(c.pitchedCommonName)
	c.addLyric(c.normalFormString)	
	c.addLyric(c.forteClassTn)
	s.append(c)
	### uma nota menos 1 semitom
	intervalo=interval.Interval(-1)
	t=c1[n].transpose(intervalo)
	c=chord.Chord([t,c1[((n+1)%3)],c1[((n+2)%3)]],duration=d)
	c.addLyric(c1[n].name +' menos 1 Semitom')
	c.addLyric(c.pitchedCommonName)
	c.addLyric(c.normalFormString)	
	c.addLyric(c.forteClassTn)
	s.append(c)

	### duas primeiras notas mais 1 semitom
	intervalo=interval.Interval(+1)
	t1=c1[n].transpose(intervalo)
	e2=c1[((n+1)%3)]
	t2=e2.transpose(intervalo)
	c=chord.Chord([t1,t2,c1[((n+2)%3)]],duration=d)
	c.addLyric(c1[n].name+' mais 1 Semitom')
	c.addLyric(e2.name+' mais 1 Semitom')
	c.addLyric(c.pitchedCommonName)
	c.addLyric(c.normalFormString)	
	c.addLyric(c.forteClassTn)
	s.append(c)

	### duas primeiras notas menos 1 semitom
	intervalo=interval.Interval(-1)
	t1=c1[n].transpose(intervalo)
	e2=c1[((n+1)%3)]
	t2=e2.transpose(intervalo)
	c=chord.Chord([t1,t2,c1[((n+2)%3)]],duration=d)
	c.addLyric(c1[n].name+' mais 1 Semitom')
	c.addLyric(e2.name+' mais 1 Semitom')
	c.addLyric(c.pitchedCommonName)
	c.addLyric(c.normalFormString)	
	c.addLyric(c.forteClassTn)
	s.append(c)

	### primeira e ultima notas mais 1 semitom
	intervalo=interval.Interval(+1)
	t1=c1[n].transpose(intervalo)
	e2=c1[((n+2)%3)]
	t2=e2.transpose(intervalo)
	c=chord.Chord([t1,t2,c1[((n+2)%3)]],duration=d)
	c.addLyric(c1[n].name+' mais 1 Semitom')
	c.addLyric(e2.name+' mais 1 Semitom')
	c.addLyric(c.pitchedCommonName)
	c.addLyric(c.normalFormString)	
	c.addLyric(c.forteClassTn)
	s.append(c)

	### primeira e ultima notas menos 1 semitom
	intervalo=interval.Interval(-1)
	t1=c1[n].transpose(intervalo)
	e2=c1[((n+2)%3)]
	t2=e2.transpose(intervalo)
	c=chord.Chord([t1,t2,c1[((n+2)%3)]],duration=d)
	c.addLyric(c1[n].name+' mais 1 Semitom')
	c.addLyric(e2.name+' mais 1 Semitom')
	c.addLyric(c.pitchedCommonName)
	c.addLyric(c.normalFormString)	
	c.addLyric(c.forteClassTn)
	s.append(c)







s.show('midi')
s.show('lily.pdf')
 
 
 







