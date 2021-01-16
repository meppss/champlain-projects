# variables
i = 0
# iterate from i until 9
while (i < 10):
    # if the remainder of i divided by 2 equals 0, then print i and increment i by 1
    if i % 2 == 0:
        print(i)
        i = i + 1
    else:
        # if the remainder is more than zero, only increment i by 1, then continue to the next iteration.
        i = i + 1
        continue
