#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   HIGASHI Koichi
# Created:  2014-03-13
#
import sys
from optparse import OptionParser
import re
import itertools
eco = {
        'target':re.compile(r'GAATTC', re.IGNORECASE),
        'padding':1
}
hind = {
        'target':re.compile(r'AAGCTT', re.IGNORECASE),
        'padding':1
}
bam = {
        'target':re.compile(r'GGATCC', re.IGNORECASE),
        'padding':1
}
noti = {
        'target':re.compile(r'GCGGCCGC', re.IGNORECASE),
        'padding':2
}

def loadFasta(infile):
    seq = ''
    firstLine = True
    for line in open(infile):
        if firstLine:
            firstLine = False
            continue
        seq += line.rstrip()
    return seq

def restriction(seq, ecoRI=True, hindIII=True, bamHI=True, notI=True):
    positions = []
    if ecoRI:
        iterator = eco['target'].finditer(seq)
        for match in iterator:
            positions.append(match.start() + eco['padding'])
    if hindIII:
        iterator = hind['target'].finditer(seq)
        for match in iterator:
            positions.append(match.start() + hind['padding'])
    if bamHI:
        iterator = bam['target'].finditer(seq)
        for match in iterator:
            positions.append(match.start() + bam['padding'])
    if notI:
        iterator = noti['target'].finditer(seq)
        for match in iterator:
            positions.append(match.start() + noti['padding'])
    positions = list(set(positions))
    positions.sort()
    positions = [0] + positions + [len(seq)]
    diff = []
    for (i,j) in itertools.combinations(positions,2):
        diff.append(j-i)
    diff.sort()
    return diff

if __name__ == '__main__':
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file", action="store", type="string", dest="infile", help="input single FASTA file")
    parser.add_option("-E", "--EcoRI", action="store_true", default=False, help="use EcoRI")
    parser.add_option("-H", "--HindIII", action="store_true", default=False, help="use HindIII")
    parser.add_option("-B", "--BamHI", action="store_true", default=False, help="use BamHI")
    parser.add_option("-N", "--NotI", action="store_true", default=False, help="use NotI")
    (options, args) = parser.parse_args()
    if options.infile == None:
        parser.print_help() 
        sys.exit(1)
    seq = loadFasta(options.infile)
    length = restriction(seq, ecoRI=options.EcoRI, hindIII=options.HindIII, bamHI=options.BamHI, notI=options.NotI)
    for l in length:
        print l
