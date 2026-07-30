arr = [12, 45, 7, 89, 34]


largest = arr[0]

largest_index = 0

for i in range(len(arr)):
    if( arr[i] > largest ):
        largest = arr[i]
        largest_index = i
      
print(largest)
print(largest_index)

        