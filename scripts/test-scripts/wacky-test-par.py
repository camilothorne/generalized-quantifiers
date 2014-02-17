#!/usr/bin/python


# Custom libraries


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


from proporpar import *
import multiprocessing
from multiprocessing import Pool


# Corpora root files and format


# N.B. Some corpora are stored in /usr/lib/nltk_lite/
# while custom corpora are stored elsewhere


# Original + wacky 1M subset


plotting = '/home/professors/cathorne/Desktop/quantifiers/wacky-script/plotting-test'
path     = "/home/professors/cathorne/Desktop/quantifiers/wacky-script/corpus-small/"
format   = ".*test"
list     = ('avg','cumul','brown','clinical','geo','trec','ukwack')


# Ramsey GQs (Jakub)


if __name__ == '__main__':
    cpu = multiprocessing.cpu_count()
    pool = Pool(processes=(cpu))                                    # start k worker processes
    ProporStats(path,format,list,plotting,pool)
    #pool.close()
    #pool.join()