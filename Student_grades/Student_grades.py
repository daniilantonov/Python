def reading_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        dict = {}
        for line in file:
            name, value = line.split(',')
            dict[name] = dict.get(name, []) + [int(value.rstrip('\n'))]

    return dict

def save_result(dict):
    for key, value in dict.items():
        mini = min(value)
        sred = sum(value) / len(value)
        maxi = max(value)
    with open('output.txt', 'a+', encoding='utf-8') as file:
            file.write(f'{key}-{mini}, {sred}, {maxi} \n')


save_result(reading_data('input.txt'))