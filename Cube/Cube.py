import random 
instruction =str(print("Введите: 1 чтобы бросить кубик, 2 чтобы выйти"))
player_name= str(input('Введите имя : '))


while True:
    player_input= int(input('Введите число : '))
    if player_input == 2 :
        break
    elif player_input == 1:
        hidden_number = random.randint(0,6)
        print(f"Cube {hidden_number}")
    else: 
        print("Вы ввели неверную команду")
        break
        
print("Спасибо за игру")




