#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   HIGASHI Koichi
# Created:  2014-03-14
#
ECs = []
for line in open('./enzyme_randomized.list'):
    EC = dict.fromkeys(['canonicalNumber', 'line'])
    EC['line'] = line
    n = line.rstrip().split()[0].split(':')[1].split('.')
    EC['canonicalNumber'] = int('%03d%03d%03d%03d'%(int(n[0]), int(n[1]), int(n[2]), int(n[3])))
    ECs.append(EC)

ECs.sort(cmp=lambda x,y:cmp(x['canonicalNumber'], y['canonicalNumber']))

ofp = open('./enzyme_sorted.list','w')
for ec in ECs:
    ofp.write(ec['line'])
ofp.close()
