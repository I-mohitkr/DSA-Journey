arr = [1, 2, 3, 4, 5, 6]
sum = 0
for i in arr:
   square = i*i
   if square % 3 == 0:
      sum = sum + square
print(sum)