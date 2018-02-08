# Names Assignment

# Part I
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
i = 0
while i < len(students):
    print students[i]["first_name"] + " " + students[i]["last_name"]
    i += 1

# Part II
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
print ("Students")
i = 0
while i < len(users["Students"]):
    print ('{} - ' + users["Students"][i]["first_name"] + ' ' + users["Students"][i]["last_name"]).format(i+1)
    i += 1

print ("Instructors")
y = 0
while y < len(users["Instructors"]):
    print ('{} - ' + users["Instructors"][y]["first_name"] + ' ' + users["Instructors"][y]["last_name"]).format(y+1)
    y += 1

# END