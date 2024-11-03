dna_input = "GCAT"
dna_output = ""

for nucleotide in dna_input:
    if nucleotide == "G":
        dna_output += "C"
    elif nucleotide == "C":
        dna_output += "G"
    elif nucleotide == "A":
        dna_output += "T"
    elif nucleotide == "T":
        dna_output += "A"

print(dna_output)