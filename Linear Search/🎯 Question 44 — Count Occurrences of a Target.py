arr = [10, 25, 8, 19, 25, 30, 25]
target = 25
count = 0
for i in range(len(arr)):
     if (arr[i] == target):
         count = count + 1
print(count)