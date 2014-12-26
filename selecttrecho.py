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



#searchStream1 = stream.Stream()
#searchStream1.append(note.Note(quarterLength = 2.0))
#l = search.rhythmicSearch(maodir, searchStream1)



