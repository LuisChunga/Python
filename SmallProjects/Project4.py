#!/usr/bin/env python3

# Luis Chunga
# Project 4
# Doc string description of project

"""
This program will read a file of sequence ids and sequences
from the file named as the second command-line argument.  All test input
files will be some subset of the lines in p4sampin.  Note that p4sampin
has each id and its sequence on the same line.

This program will compare all pairs of lines and print out the seqids
for the two sequences that have the Longest Common Substring.  A small
function in p4starter.py will be used to perform the calculation for each
pair of strings.

In short, this program will do a simple all-to-all comparison, i.e each
sequence will be compared against every other sequence.  The program
does not need to skip comparisons that have already been done by any
process.

"""

import time
import multiprocessing as mp
import sys

file = open(sys.argv[2])
processor = int(sys.argv[1])

seqid = []           #Create an empty list
sequence = []        #Create an empty list
for line in file:    #iterate line in file
    seqid.append(line.split()[0])   #Adds index 0 of split line to seqid 
    sequence.append(line.split()[1])#Adds index 1 of split line to sequence

#From p4starter.py (Determines longest common string)
def lcs(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])

    return lcs_set

#From NOTES_MUTIPROC (02_process_ques.py file) with modification for project4
def worker_bee(a, b, num_lines, q):
    s = []    #This will hold ID and longest string
    longest = 0
    for index in range(a, b):		
        for index2 in range(num_lines):
            if index == index2: #Compares index for similarities 
                continue
            #Return longest common string (lcs) to lcs function
            ret = list (lcs (sequence[index], sequence[index2]))
            if longest < len(ret[0]):  #Looks for the longest string
                longest = len(ret[0])
                seqid1 = index       #Assign index to seqid1
                seqid2 = index2      #Assign index2 to seqid2

    s.append(longest)          #Adds longest string to list 
    s.append(seqid[seqid1])    #Adds first sequence ID to list 
    s.append(seqid[seqid2])    #Adds second sequence ID to list
    
    q.put(s)  #Places data to queue

procs= []
q = mp.Queue()

#Divide the total number of lines of sequence by the number of processors
#to determine how many lines each process processes
chunk = int(len(sequence) / processor) 
remainder = (len(sequence) % processor) #Calculates remainer of processor
for i in range (processor):
    lo = i * chunk
    hi = (i+1) * chunk
    if i == (processor-1):
        hi += remainder #adds remainder to last processor
    #Assign number of elements in sequence to num_lines variable 
    num_lines = len(sequence) 
    p = mp.Process(target=worker_bee, args=(lo,hi,num_lines, q))
    procs.append(p)

startTime = time.time()
for p in procs:
    p.start()

for p in procs:
    p.join()
#   it prints the time that it takes
#   print( "%0.4f" % (time.time() - startTime) )

s = 0
maximum = 0
for p in procs:
    s = q.get()
    if maximum < s[0]:   #Compares longest strings among processors
        maximum = s[0]
        seqid1 = s[1]
        seqid2 = s[2]

print(' ', maximum, seqid1, seqid2)


