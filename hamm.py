dna1 = "GAGCCTACTAACGGGAT"
dna2 = "CATCGTAATGACGGCCT"

result = 0
idx = 0

for element in dna1:
    if element != dna2[idx]:
        result += 1
        idx += 1
    elif element == dna2[idx]:
        idx += 1

print (result)