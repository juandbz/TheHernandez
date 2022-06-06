size = 5
#block size and 1st gen
count = 0
#start with the first letter A
for o in range(size):
    for s in range(size):
        print(chr(65 + count), end=" ")
        count += 1
    print()