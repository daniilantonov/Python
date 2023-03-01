from collections import defaultdict

def reading_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        student_grades = defaultdict(list)
        for line in file:
            value = line.strip().split(',')
            if len(value) != 2:
                raise Exception('File structure not valid')
            name = value[0]
            grade = int(value[1])
            student_grades[name].append(grade)
    return student_grades

def save_result(result):
    with open('output.txt', 'w', encoding='utf-8') as file:
        for student_name, grades in result.items():
            min_grade = min(grades)
            average_grade = sum(grades) / len(grades)
            max_grade = max(grades)
            file.write(f'{student_name}:{min_grade}, {average_grade}, {max_grade}\n')
            
save_result(reading_data('input.txt'))