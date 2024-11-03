input_dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    
result = []

counterA = 0
counterT = 0
counterG = 0
counterC = 0


for character in input_dna:
    if character == ('A'):
        counterA += 1
    if character == ('T'):
        counterT += 1
    if character == ('G'):
        counterG += 1
    if character == ('C'):
        counterC += 1
result = [counterA, counterC, counterG, counterT]
print (result)
