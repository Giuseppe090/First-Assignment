n = 5
k = 3
result = 0

if n <= 2:
    result = +1
else:
    result = n-1 + k + k * (n-2) + k

print (result)