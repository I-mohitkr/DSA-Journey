arr = [5, 2, 8, 1, 9]

largest = arr[0]
smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i
    elif i > largest:
        largest = i

diff = largest - smallest
print(diff)