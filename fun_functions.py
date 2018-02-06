# Fun with Functions Assignment

# Odd/Even
for number in range (1, 20001):
    if number % 2 == 0:
        print ('Number is {}. This is an odd number.').format(number)
    if number % 2 != 0:
        print ('Number is {}. This is an even number.').format(number)

# Multiply
def multiply():
    a = [2,4,10,16]
    i = 0
    while i < len(a):
        a[i] = a[i] * 5
        i += 1
    print (a)

multiply()

# Hacker Challenge
def hackerchallenge():
    x = [2,4,5]
    i = 0
    new = []
    while i < len(x):
        x[i] = (("1" * x[i]) * 3)
        i += 1
    new_x = x[0:1]
    new_xx = x[1:2]
    x = x[2:3]
    new.insert(0, new_x)
    new.insert(1, new_xx)
    new.insert(2, x)

    print new

hackerchallenge()

# END