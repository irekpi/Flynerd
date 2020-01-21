# -*- coding: utf8 -*-
# zmiana miejsc, zastepowanie znakow i liczenie

DNA='ACTGTGCTGACTCCCGGTGCTGCCGCTGCCATAGCTAAAGCCCGGGTCCTGGTAGGCAGGCGGGAAGCAG'

DNA.upper()
DNA.replace(' ', '')
print(DNA, '\n')

A = DNA.count('A')
C = DNA.count('C')
T = DNA.count('T')
G = DNA.count('G')
print('A = {}, C = {}, T = {}, G = {}' .format(A, C, T, G))
