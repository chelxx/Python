# Type List Assignment

x = ["mermaid", 23, "unicorn", 1990, "dragon"]
i = 0
while i < len(x):
    if type(x[i]) is int:
        print "Add 100 to that and it's:", x[i] + 100,  "- I'm an integer!"
    if type(x[i]) is str:
        print ("Oh my! It's a " + x[i] + "! - I'm a string!")
    i += 1

# END