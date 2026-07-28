arr = [2, 3, 4, 6]
mul = 1
for i in arr:
    square = i*i
    if(square % 3 == 0):
        mul = mul * square

print(mul)