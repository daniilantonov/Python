def read_grades(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        dict = {}
        grades_dict = {}
        for line in file:
            name,value  = line.split(',')
            dict[name] = dict.get(name, []) + [int(value.rstrip('\n'))]
            if name not in grades_dict:
                grades_dict[name] = []
            else:
                grades_dict[name].append()
        return grades_dict

def write_stats(grades_dict, output_file):
    with open(output_file, 'w') as f:
        for name, grades in grades_dict.items():
            min_grade = min(grades)
            max_grade = max(grades)
            avg_grade = sum(grades) / len(grades)
            f.write(f"{name},{min_grade},{avg_grade:.2f},{max_grade}\n")

grades_dict = read_grades('input.txt')
write_stats(grades_dict, 'output.txt')