# Stars Assignment

# Part I
def draw_stars():
    x = [4, 6, 1, 3, 5, 7, 25]
    i = 0
    while i < len(x):
        x[i] = x[i] * '*'
        print x[i]
        i += 1

draw_stars()

# Part II
def draw_stars():
    x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
    i = 0
    while i < len(x):
        if type(x[i]) is str:
            x[i] = i * x[i][0]
            print x[i]
        else:
            x[i] = x[i] * '*'
            print x[i]
        i += 1

draw_stars()

# END