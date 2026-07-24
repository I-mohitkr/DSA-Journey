arr = [2, 5, 3, 4]
result = []
largest = 0
for i in arr:
    square = i*i
    if square > largest:
        largest = square
print(largest)
