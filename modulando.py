from music21 import *

#sensvel mais proxima
c1= chord.Chord('E4 G4 C5')
L = analysis.neoRiemannian.L(c1)


#relativa mais proxima
c2= chord.Chord('E4 C4 G4 C5')
R = analysis.neoRiemannian.R(c2)

#relativa da sensivel
Rl = analysis.neoRiemannian.R(L)

#sensivel da relativa da sensivel
SRl = analysis.neoRiemannian.R(Rl)

#acorde dos intervalos inversos 
#E4 G4 C5 -> 0 3 8 -> 0 9 4 -> 0 4 9 -> E4 G#4 C#4
#i= chord.Chord('C4 E4 G#4 C#5')

Emin=chord.Chord('B3 E4 G4')
Esem=chord.Chord('B3 E4 B4')
dom=chord.Chord('C4 F#4 C5')
Cmajmin=chord.Chord('C4 G4 C5')
Amajmin=chord.Chord('A3 A4 E4')
A6=chord.Chord('C4 A4 E4')
Cmaj=chord.Chord('C4 G4 E4')
E64=chord.Chord('B3 G4 E4 B4')
E6=chord.Chord('G3 B4 E4 E5',duration=duration.Duration(0.5))
Bmaj=chord.Chord('F#3 B4 D#4 F#5',duration=duration.Duration(2.5))
Emaj=chord.Chord('E3 B4 E4 G5',duration=duration.Duration(1.0))

#adicionando graus de funcionalidade relativos a do
def printagrau(tonalidade,acorde):
	r=roman.romanNumeralFromChord(acorde,key.Key(tonalidade))
	acorde.addLyric(r.figure)

K='e'#tonalidade

printagrau(K,L)
printagrau(K,c1)
printagrau(K,c2)
printagrau(K,R)
printagrau(K,Rl)
printagrau(K,SRl)
printagrau(K,Emin)
printagrau(K,Esem)
printagrau(K,dom)
printagrau(K,Cmajmin)
printagrau(K,Amajmin)
printagrau(K,A6)
printagrau(K,Cmaj)
printagrau(K,E64)
printagrau(K,E6)
printagrau(K,Bmaj)
printagrau(K,Emaj)

s=stream.Stream( )
s.append(L)
s.append(c1)
s.append(c2)
s.append(R)
s.append(Rl)
s.append(SRl)
s.append(Emin)
s.append(Esem)
s.append(dom)
s.append(Cmajmin)
s.append(Amajmin)
s.append(note.Note('B3'))
s.append(A6)
s.append(Cmaj)
s.append(note.Note('D#4'))
s.append(E64)
s.append(E6)
s.append(Bmaj)
s.append(Emaj)
s.append(note.Note('E5',duration=duration.Duration(4.0)))



s.show('midi')
s.show('lily.pdf')
