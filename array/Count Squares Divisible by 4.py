arr = [1, 2, 3, 4, 5, 6]
count = 0
for i in arr:
    square = i*i
    if square % 4 == 0:
        count = count+1
print(count)