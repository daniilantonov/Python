def input_file(file_):
    with open(file_, 'r', encoding='utf-8') as file:
        dct = {}
        for line in file:
            name, value = line.split(',')
            dct[name] = dct.get(name, []) + [int(value.rstrip('\n'))]

    return dct

def output_file(dct):
    for key, value in dct.items():
        mini = min(value)
        sred = sum(value) / len(value)
        maxi = max(value)
        with open('output.txt', 'a+', encoding='utf-8') as file:
            file.write(f'{key}-{mini}, {sred}, {maxi} \n')


output_file(input_file('input.txt'))