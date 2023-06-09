s = open('rosalind_dna.txt', 'r')
sequence = s.read()

A = 0 
C = 0
G = 0
T = 0

for nucleotide in sequence:
    if nucleotide == 'A': 
        A +=1
    elif nucleotide == 'C': 
        C +=1
    elif nucleotide == 'G': 
        G +=1
    elif nucleotide == 'T': 
        T +=1
        
print(A, C, G, T)


