# Find Characters Assignment

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []
i=0
while i < len(word_list):
    if char in word_list[i]:
        new_list.append(word_list[i])
    i += 1

print new_list

# END