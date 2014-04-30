#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   HIGASHI Koichi
# Created:  2014-03-14
#

# 4のコード、矢野くんに怒られたので改変

ECs = []
for line in open('./enzyme_randomized.list'):
    EC = dict.fromkeys(['numbers', 'line'])
    EC['line'] = line
    EC['numbers'] = [ int(x) for x in line.rstrip().split()[0].split(':')[1].split('.') ]
    ECs.append(EC)

ECs.sort(cmp=lambda x,y:cmp(x['numbers'], y['numbers']))

ofp = open('./enzyme_sorted.list','w')
for ec in ECs:
    ofp.write(ec['line'])
ofp.close()
