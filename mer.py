A = (2, 4, 10, 18)
B = (-5, 11, 12)


C = []
i, j = 0, 0
while i < len(A) and j < len(B):
    if A[i] <= B[j]:
        C.append(A[i])
        i += 1
    else:
        C.append(B[j])
        j += 1
	
C += A[i:]
C += B[j:]

print (C)