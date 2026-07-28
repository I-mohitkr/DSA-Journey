arr = [2, 5, 3, 6, 1]
number = 20
count = 0
for i in arr:
    square = i * i
    if (square > number):
        count = count + 1
print(count)