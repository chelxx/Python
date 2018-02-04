# Scores and Grades Assignments

for x in range (10):
    rand_num = random.randint(60, 101)
    if rand_num <= 100 and rand_num >= 90:
        print ('Score: {}; Your grade is A.').format(rand_num)
    if rand_num <= 89 and rand_num >= 80:
        print ('Score: {}; Your grade is B.').format(rand_num)
    if rand_num <= 79 and rand_num >= 70:
        print ('Score: {}; Your grade is C.').format(rand_num)
    if rand_num <= 69 and rand_num >= 60:
        print ('Score: {}; Your grade is D.').format(rand_num)

# END