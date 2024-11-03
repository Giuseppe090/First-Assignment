string1 = "GATATATGCATATACTT"
string2 = "ATAT"
locat = []
for i in range(len(string1)):
    if string2 == string1[i: i+len(string2)]:
        locat.append(i+1)
print (locat)
