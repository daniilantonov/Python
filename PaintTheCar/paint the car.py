def paint_car(car, new_color):
    print(f"Old color {car['color']} -> New color {new_color}")
    car['color'] = new_color
    return car
car = {
   'color': 'red',
   'brand': 'BMW',
   'year': 2015,
   'horsepower': 320
}

paint_car(car,'green')
print(car)



def increase_horsepower(car, increase_by):
    new_horsepower = car ['horsepower'] + increase_by
    print(f"horsepower up {car['horsepower']} -> {car['horsepower'] + increase_by}")
    car ['horsepower'] = new_horsepower
    return car

car = {
   'color': 'red',
   'brand': 'BMW',
   'year': 2015,
   'horsepower': 320
}

increase_horsepower(car,25)
print(car)
