# Luis  Chunga
# Project 2
# Doc string description of project
"""
This programm will find all potential genes (codons in the same reading frame)
in a sample set of DNA data. The DNA data will be no less than 33 bytes and no
more than 99 bytes long, including the start and stop codons.  Start codons are
all either ATG or GTG, and stop codons are all TAG.  Both lower and upper case are
accepted.  Not all characters in the input will necessarily be a,c,g,t.
This program will merely look for valid codons and accept all substrings between
the codons that are of the correct length.

A gene is terminated by the stop codon nearest to its start codon in the same
reading frame.  Some genes may overlap, perhaps in different reading
frames, or two genes may even share a stop codon in the same reading frame.

The input filename will be the only command-line arg.
The input will consist of lines containing a seqid followed by an arbitrary
amount of whitespace then a character sequence.
"""



import sys

# Opens text file through sys that is passes as a command argument
infile = open(sys.argv[1])

# Priming read
line = infile.readline().split()

# Reads file (list) until it is empty
while line != []:
    dna = line[1].lower()  # Converts letters to lowercase
    for i in range(len(dna)):
                # Looks at sequence into increments of 3 and looks for start codon
                if(dna[i:i+3]) == "atg" or (dna[i:i+3]) == "gtg":             
                    start = i
                    for index in range(i,len(dna)):
                        # Locates end codon of DNA sequence
                        if(dna[index:index+3]) == "tag":               
                            end = index
                            size = (end + 3)-(start)  # Calculates size of codon
                            # Condition needed to satisfy DNA sequence
                            if size >= 33 and size <= 99 and (size % 3 == 0):  
                                print ('{:35}'.format(line[0]), '{:3}'.format(start),\
                                       '{:3}'.format(size),'{:3}'.format(dna[i:i+3]),\
                                       '{:3}'.format(dna[index:index+3]) )
                                break
    # Recurring Read                           
    line = infile.readline().split()
                    
