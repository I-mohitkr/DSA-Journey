arr = [5, 2, 8, 1]
smallest = arr[0] * arr[0]
for i in arr:
    square = i * 1
    if square < smallest:
       smallest = square
print(smallest)