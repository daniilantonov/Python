import random
number = int(input('Numbers of user  >> '))
man_name = ['Dmitry', 'Artem','Slavik']
woman_name = ['Katerina','Diana','Anna']
age_min , age_max = 10, 50 
nationals = ['European','Asian']
state = ['female','male']

for _ in range(number):
    age = random.randint(age_min , age_max)
    state_random = random.choice(state)
    random_nation = random.choice(nationals) 
    if state_random == 'male':
        random_name = random.choice(man_name)
        
    else : 
        random_name = random.choice(woman_name)
    
    random_user = dict(
        name = random_name ,
        age = age,
        nationals =  random_nation,
        state = state_random,

        )
    print(random_user)