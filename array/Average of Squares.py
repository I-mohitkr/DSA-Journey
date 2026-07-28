arr = [1, 2, 3, 4]
sum = 0
count = 0
for i in arr:
    square = i*i
    sum = sum + square
    count = count + 1
    average = sum/count
print(average)