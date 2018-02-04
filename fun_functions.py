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