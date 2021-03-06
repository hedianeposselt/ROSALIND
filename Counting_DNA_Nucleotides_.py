# https://rosalind.info/problems/dna/
# Counting DNA Nucleotides exercise from ROSALIND


dataset = "GTTAATAGACTTGCGCGAGACGTCCCTATACCTGATCTCGCGAGTTTAAAATTAGCTTTTTTAGAGTAGCGTACTCTACGAGGGATATAAGCGCCAAAGAGTTGTTGCCGATATCGTTCAGCCCCAAGCGACAACAATTGCACAACCGAAACTGTCAAACATCGAGATACGAGAGCTATGGATGATGTCAGGAGTGGGAGGCGCGCCAACTCCCTTACCGACGAACCTGAACGATGGTCTCTAGATATACAAATCTGGGCGCGTTGTCTTTGGTAGGCTTATGAAGGTCACTAAAGGTACCCGCTATCCGCTATTCACATCGGGCAATCAACTGTCAACTACCGAAATCGTGCACTTTACTCATCCGTGTAGGTCGAATCGGGCTGACTCGCGTTCCGGACGAGAAATTTGTGTATGGTGCGCGCTTATAATCACCGGCCTTCGTAGAGTATTTATTCTTCGTTCGGAGGATAGCGCTGGAAACCCCTTTAAGAATTGGCGGTGTCATGCCAACCCTTTAATCCGCATACGTCGAGCTGACACAGCTCGATTGGCGTGTGCCCCTTCACTTTCGACCGTTCTTCTCGTCGCGGATGACAGATAATAGCTGAGCGTGGCGTCCTTACACGCAGCTACCAGGAGATGAGGTACAACCGTCGGATGTTGGGATTCCTAGTAGGGCGATGCGCAGTCCACCCTAACCCCGAGCAGCCAGCTGCGTGTCTACTAACCCGAGAGTCTGCCTGCCACCTGTTGACATTCACGTGCGGCGACTGGAACCGATCTACCAAGCGACTGTTCGCGGATTGTCAAGGGTCATCGGAGGAGAATAGTTCGGCTCTTCTGTTGAAGACAATGCGCCAGGGCCATAAAATGCTCGGAGAACCCAGTTAGCGTGTTCTAAGCGCGCATTTGCCGCGTAATCGTACTGTGACCACCACGTGCAGTGTATAAGGTGGGGGTGTGCTGCTGCTCGGAACGCGCAGTGCAGCCGTGAAGG"

A = dataset.count("A")
C = dataset.count("C")
G = dataset.count("G")
T = dataset.count("T")

print (A, C, G, T)