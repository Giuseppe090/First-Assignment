pop1 = 2
pop2 = 2
pop3 = 2

i = pop2 * pop2 + 4 * pop3 * pop3 + 4 * pop2 * pop3 - 4 * pop3 - pop2
j = 4 * (pop1 + pop2 + pop3) * (pop1 + pop2 + pop3 - 1)
prob = 1 - i / j

print (prob) #se vogliamo la percentuale di probabilità allora 
#print (prob*100)