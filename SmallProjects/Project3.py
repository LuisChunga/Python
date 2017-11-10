#!/usr/bin/env python3

# Luis Chunga
# Project 3
# Doc string description of project
"""
This program creates a python3 module named p3mod.py which can be
imported and used as in the sample p3rmb.py program.

The module will provide the function named read_one_fasta_entry which
takes in an open file as an argument.  That function is implemented
as a generator which will, on each invocation, return a single entry
from a fasta file (e.g. p3sampin).

Note1:  the ">" symbol is *NOT* part of the pegid.
Note2:  the pegid is terminated by the first whitespace on the line.
"""



#This is on a different file

import sys

import p3mod


f = open(sys.argv[1])
for (pegid,protseq) in p3mod.read_one_fasta_entry(f):
    print(pegid,protseq)
f.close()


______________________________________________________________



def read_one_fasta_entry(f):
    pegid = None             #Nonetype class to represent NULL
    protseq = []             #Create an empty list
    for line in f:           #iterate line in file
        if line[0] == '>':   #Locate '>' symbol and omit for pegid
            if pegid:
                yield (pegid, protseq)
            pegid = line[1:-1].split()[0] #Set pegid location index[0]
            protseq = ''                  #Set protseq to empty string 
        else:
            protseq += line[:-1]          #Join protseq into single line
    yield (pegid, protseq)

