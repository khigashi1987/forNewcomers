#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   HIGASHI Koichi
# Created:  2014-03-13
#

import itertools

Codon_Table = {
        'A':['GCT','GCC','GCA','GCG'],
        'C':['TGT','TGC'],
        'D':['GAT','GAC'],
        'E':['GAA','GAG'],
        'F':['TTT','TTC'],
        'G':['GGT','GGC','GGA','GGG'],
        'H':['CAT','CAC'],
        'I':['ATT','ATC','ATA'],
        'K':['AAA','AAG'],
        'L':['TTA','TTG','CTT','CTC','CTA','CTG'],
        'M':['ATG'],
        'N':['AAT','AAC'],
        'P':['CCT','CCC','CCA','CCG'],
        'Q':['CAA','CAG'],
        'R':['CGT','CGC','CGA','CGG','AGA','AGG'],
        'S':['TCT','TCC','TCA','TCG','AGT','AGC'],
        'T':['ACT','ACC','ACA','ACG'],
        'V':['GTT','GTC','GTA','GTG'],
        'W':['TGG'],
        'Y':['TAT','TAC'],
        '*':['TAA','TAG','TGA']
}

def aa2dna(aaseq):
    patterns = []
    for aa in aaseq:
        patterns.append(Codon_Table[aa])
    dnaseqs = []
    for x in itertools.product(*patterns):
        dnaseqs.append(''.join(list(x)))
    return dnaseqs

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print 'usage: python %s AA-seq\n'%sys.argv[0]
        sys.exit(1)
    aaseq = sys.argv[1].upper()
    DNAseqs = aa2dna(aaseq)
    for i,dnaseq in enumerate(DNAseqs):
        print (i+1),'\n',dnaseq
