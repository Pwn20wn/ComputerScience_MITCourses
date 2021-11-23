#default values are start = 0 and step = 1
# and option loop until value is stop -1

mysum = 0
for i in range(7, 10):
    mysum += i
    print(mysum)

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
        mysum += 1
print(mysum)