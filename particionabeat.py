from music21 import *
score = converter.parse('localcorpus/mikro041.xml')
partBass = score.getElementById('P1-Staff2')
ts = partBass.flat.getElementsByClass('TimeSignature')[0]
ts.beatSequence.partition(1)

'''
for h in range(len(ts.beatSequence)):
	ts.beatSequence[h] = ts.beatSequence[h].subdivide(3)
	for i in range(len(ts.beatSequence[h])):
		ts.beatSequence[h][i] = ts.beatSequence[h][i].subdivide(2)
		for j in range(len(ts.beatSequence[h][i])):
			ts.beatSequence[h][i][j] = ts.beatSequence[h][i][j].subdivide(8)
'''
for m in partBass.getElementsByClass('Measure'):
	for n in m.notesAndRests:
		for i in range(ts.getBeatDepth(n.offset)):
			n.addLyric('*')

partBass.getElementsByClass('Measure')[0:7].show('lily.pdf')  
