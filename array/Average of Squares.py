arr = [1, 2, 3, 4]
sum = 0
length = len(arr)
for i in arr:
    square = i*i
    sum = sum + square
    average = sum/length
print(average)