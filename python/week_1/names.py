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

for userType in users.keys():
    print userType
    for idx, user in enumerate(users[userType]):
        print "{} - {} {} - {}".format(idx + 1,
                                       user['first_name'].upper(),
                                       user['last_name'].upper(),
                                       len(user['first_name']) + len(user['last_name']))
