arr = [3, 5, 8, 2]

number = 50
sum = 0
for i in arr:

    square = i * i

    if(square < number):
        sum = sum + square

print(sum)