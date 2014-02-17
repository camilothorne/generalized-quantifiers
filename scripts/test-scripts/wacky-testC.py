#!/usr/bin/python


# custom libraries


import sys


sys.path.append(u'../mynltk/')


#================#
#================#
#                #
#  Stats script  #
# (init file)    #
#                #
#================#
#================#


from proporrecip import *


# 0. Corpora root files and format


# N.B. Some corpora are stored in /nltk_lite/
# while custom corpora are stored elsewhere


# brown + wacky 100M subset


plotting = '/home/professors/cathorne/Desktop/quantifiers/wacky-script/plotting-test'
path     = "/home/professors/cathorne/Desktop/quantifiers/wacky-script/corpus-small/"
format   = ".*test"
list     = ('avg','cumul','brown','clinical','geo','trec','ukwack')


# 2. Ramsey GQs (Jakub)


ProporRamsey(path, format, list, plotting)


# N.B. By quantifier class
