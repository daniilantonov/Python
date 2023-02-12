import random
number = int(input('Numbers of user  >> '))
man_name = ['Dmitry', 'Artem','Slavik']
woman_name = ['Katerina','Diana','Anna']
nationals = ['European','Asian']
state = ['female','male']

user_list=[]

for i in range(number):
    user = dict(state='',name= '',age='',nationals='')
    state_random = random.choice(state)
    if state_random == 'male':
        name_random = random.choice(man_name)
    else:
        name_random = random.choice(woman_name)
    user['state'] = state_random
    user['name'] = name_random
    user['age'] = str(random.randint(10,50))
    user['nationals'] = random.choice(nationals)

    user_list.append(user)
print(user_list)
