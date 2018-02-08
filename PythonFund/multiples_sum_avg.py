# Multiples, Sum, Average Assignment

# Multiples Part I
for count in range(1, 1001):
    print count

# Multiples Part II
five = 5
for num in range (1000000):
    if num % 5 == 0:
        five = num
        print five

# Sum List
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b

# Average List
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
avg = b / len(a)
print avg

# END