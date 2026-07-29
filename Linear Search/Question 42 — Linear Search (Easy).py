arr = [10, 25, 8, 19, 30]
target = 19

for i in arr:
    if ( target == i):
        found = True
        break
    else:
     found = False

if(found):
    print("found")
else:
    print("not found")