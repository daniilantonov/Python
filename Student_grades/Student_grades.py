def reading_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        my_dict = {}
        for line in file:
            name, value = line.split(',')
            my_dict[name] = my_dict.get(name, []) + [int(value.rstrip('\n'))]
    return my_dict


def save_result(my_dict):
    with open('output.txt', 'w', encoding='utf-8') as file:
        for key, value in my_dict.items():
            mini = min(value)
            average = sum(value) / len(value)
            maxi = max(value)
            file.write(f'{key}-{mini}, {average}, {maxi}\n')
            
            
<<<<<<< HEAD
save_result(reading_data('input.txt'))
=======
save_result(reading_data('input.txt'))
>>>>>>> 5605cacc0bec369d34e9e13b95043d98af26af6c
