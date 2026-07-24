arr = [1, 2, 3, 4, 5]
count = 0
for i in arr:
    square = i*i
    if square > 10:
        count += 1
print(count)