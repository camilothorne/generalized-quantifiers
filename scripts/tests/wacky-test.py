#!/usr/bin/python


# custom libraries


import sys


sys.path.append(u'/home/camilothorne/worskspace/corpus-pkg/mynltk/')
sys.path.append(u'../wacky/')

#================#
#================#
#                                           #
#  Stats script                   #
# (init file)                         #
#                                           #
#================#
#================#


from proporB import *


# Corpora root files and format


# N.B. 1. Some corpora are stored in /usr/lib/nltk_lite/
# while custom corpora are stored elsewhere


# original + wacky 1M subset


plotting = '/home/camilothorne/plotting-test/'
path     = "/home/camilothorne/plotting-test/wacky-simple/"
format   = ".*test"
list     = ('brown','clinical','geo','trec','ukwack')


# Ramsey GQs (Jakub)


ProporStats(path, format, list, plotting)
