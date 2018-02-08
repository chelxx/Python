# String and List Practice Assignment

# Find and Replace
words = "It's thanksgiving day. It's my birthday, too!"
print words.find('day')
new_str = words.replace("day", "month", 1)
print new_str

# Min and Max
x = [2,54,-2,7,12,98]
print(max(x))
print(min(x))

# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
new_str = x[0] + x[-1]
print new_str

# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
new_x = x[0:5]
x = x[5:11]
x.insert(0, new_x)
print x

# END