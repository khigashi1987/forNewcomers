#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   HIGASHI Koichi
# Created:  2014-03-13
#

def gffParser(infile):
    genes = []
    for line in open(infile):
        if line[0] == '#':
            continue
        elems = line.rstrip().split('\t')
        if elems[2] != 'gene':
            continue
        gene = dict.fromkeys(['strand','name','start','end'])
        gene['strand'] = elems[6]
        gene['name'] = elems[-1].split(';')[1].split('=')[-1]
        gene['start'] = int(elems[3])
        gene['end'] = int(elems[4])
        genes.append(gene)
    return genes

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print 'usage: python %s gff-file\n'%sys.argv[0]
        sys.exit(1)
    infile = sys.argv[1]
    genes = gffParser(infile)
    wholeLength = 0
    for g in genes:
        wholeLength += g['end'] - g['start'] + 1
    print 'Number of genes ...',len(genes)
    print 'Whole length of coding regions ...',wholeLength,'bp'
