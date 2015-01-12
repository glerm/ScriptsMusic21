#!/usr/bin/env python
# -*- coding: utf-8 -*-
from music21 import *
import os
import sys

b=os.getcwd()+'/localcorpus/Bsonata01.xml'


MIKRO=converter.parse(b) 


MIKRO.show('lily.pdf')
