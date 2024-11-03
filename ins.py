array = [6, 10, 4, 5, 1, 2]
swap = 0
for i in range(len(array)):
    k = i
    while k > 0 and array[k] < array[k-1]:
        array[k-1], array[k] = array[k], array[k-1]
        swap += 1
        k -= 1
print(swap) 