arr = [1, 2, 3, 4, 5, 6]
largest = 0
for i in arr:
    square = i*i
    if i % 2 == 0:
     if square > largest:
        largest = square

print(largest)