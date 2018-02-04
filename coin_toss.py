# Coin Tosses Assignment

import random
heads = 0
tails = 0
toss = 0
while toss < 5001:
    cointoss = random.randint(0, 2)
    if cointoss == 0:
        tails = tails + 1
        print ("Throwing a coin and it's... tails! And there's been {} tails so far!").format(tails)
    else:
        heads = heads + 1
        print ("Throwing a coin and it's... heads! And there's been {} heads so far!").format(heads)
    toss += 1

# END