array = (4, 5, 6, 4, 1, 2, 5, 7, 4)

new_array, left_array, right_array = [], [], []
new_array.append(array[0])
for i in range(1, len(array)):
    if array[i] < array[0]:
        left_array.append(array[i])
    elif array[i] == array[0]:
        new_array.append(array[i])
    else:
        right_array.append(array[i])
new_array = left_array + new_array + right_array
print (new_array)    

#### ???? non capisco cosa non va