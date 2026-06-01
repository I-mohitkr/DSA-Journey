arr = [5, 12, 8, 20, 3, 15]
target = 10

for i in range(len(arr) - 1, -1, -1):
    if target < arr[i]:
        print(arr[i])
        break


     