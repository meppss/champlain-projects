# iterate over a range of numbers from 0 through 9
for i in range(0, 10):
    # if the remained of i divided by 2 equals 0, print i
    if i % 2 == 0:
        print(i)
    # if the remainder of i divided by 2 does not equal 0, move on to the next iteration.
    else:
        continue
