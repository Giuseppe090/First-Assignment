arr = (4, -6, 7, 8, -9, 100, 12, 13, 56, 17)
n = 10
i = 3
largest = i
l = 2 * i + 1
r = 2 * i + 2
if l < n and arr[l] < arr[largest]: 
    largest = l
if r < n and arr[r] < arr[largest]: 
    largest = r
if largest != i: 
    arr[i], arr[largest] = arr[largest], arr[i]
print(arr)

### ??? non ho idea di nulla  

