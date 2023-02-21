
import random
maximum_value=int(input("Введите максимальное значение : "))
hidden_number = random.randint(0,maximum_value)
lives = 3
player_name= str(input('Введите имя : '))


while True:
    if lives  == 0:
          print (f"Увы,{player_name},вы проиграли")
          break
    player_input= int(input('Введите число : '))
    if player_input == hidden_number:
          print (f"Ура,{player_name},вы победили  ")
          break      
    elif player_input < hidden_number:
          print("Число Меньше загаданного")
    elif player_input > hidden_number:
          print("Число Больше загаданного ")
         
    lives -= 1
   
print("Игра окончена")