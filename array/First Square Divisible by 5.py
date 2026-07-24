arr = [1, 2, 3, 4, 5, 6]
for i in arr:
    square = i * i
    if square % 5 == 0:
        break
print(square)