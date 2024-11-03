n = 11
A = (2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1)
k = 8


v = n//2
SL, SV, SR = [], [], []
for i in range(n):
    if A[i] < A[v]: SL.append(A[i])
    if A[i] == A[v]: SV.append(A[i])
    if A[i] > A[v]: SR.append(A[i])
if k <= len(SL):
    print (len(SL), SL, k)
if len(SL) < k and k <=len(SL)+len(SV):
    print(A[v])

if k > len(SL)+len(SV):
    print(len(SR), SR, k-len(SL)-len(SV))