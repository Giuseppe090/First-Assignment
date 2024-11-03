input_dna = "GATGGAACTTGACTACGTAAATT"
Nuclist = []

for element in input_dna:
    Nuclist.append(element)

idx = 0
for z in Nuclist:
    if z == 'T':
        del Nuclist [idx]
        Nuclist.insert (idx, 'U')
    idx += 1


result = ''
for y in Nuclist:
    result = result + y

print (Nuclist)
print (result)