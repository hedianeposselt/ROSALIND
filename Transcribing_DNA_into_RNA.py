# https://rosalind.info/problems/rna/
# Transcribing DNA into RNA exercise from ROSALIND

DNA = "ACAACAAAGGATCGGCGAGGAGCTGGTTAATCTCGATTCTAACAAAGGCCTCTTGAGTGACATAAAGTTGCTGTTCGGCCCCCGTTGCAGCCAAGCCTAGACTCGAGCGGGGTCTACCTCTGTAAACCCAAGTCGCAGGCCAAGGGCATTTTAACCCCCAAAGTTAGATACGTCGATTGAGTGCGCACTCCCTAACTTCAGACAGGATGGCGCTTAGCACTGGTTAGGTCCCTCATTAGAGGCTTACACGGGACCCCAGCGATCTGCAGGGCTACATGAACCGGCGATACCTGCAACCCTTCACGTGTGGTGCGAGTGCTGGACCCATGCACGGGCCCAAGAAGCGGGAGCACCCACGGCCTGAGCCTGTAGCTTCATACTTAGAGTAACACCTATAAGTTCTCCGTTTCACGTTATTTTACTTAACAAAGCACATCGATGGGCGGACGTACGAGCCGAGCCTCGTCCCCATTTACTCAAGTAACCAAGTCATTGTTTAGTCTATGGTAGGCTCTTTGATTGGGTACGCCGCAGCCATCCGCACACTTGCAGGGCTTTAGTCCGAACTCGTTCAAAGGGTTCGACGTACAACAGCGCCTACTAAATCCCCGCCTTGTAACGGAAGACGTGTGGGACCTCTTGAAACATCTTCGACCATACATCTCCATTTTAACAATGAAGCTGTATCAGTGGTCAGTCTTACTATGCCTGCACTCAGCAACAAGGGGCGCGATGATGTAGTCAGCGTGCCCAGATTCAGTACGGACAGTCAAGTGCGATCTTTCTGGGTCGCGCGGCTGGTGGTAATGAGAATGTTCTTACCTGACAAGTAATGCTTCTTCCAATCGTGCTGGGGGCAAGGTTTATTCTCTCTTAACCTGTTGCTCATCTCTAGCGATAACTGGTGCATGATCAATTTGCGG"

RNA = ""

for nucleotide in DNA:
	if nucleotide == "T":
		RNA = RNA + "U"
	else:
		RNA = RNA + nucleotide

print( RNA )