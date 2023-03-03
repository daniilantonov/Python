from collections import defaultdict

def reading_student_grades(file_path):
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

def save_accumulated_grades(student_grades , file_name):
    with open('output.txt', 'w', encoding='utf-8') as file:
        for student_name, grades in student_grades.items():
            min_grade = min(grades)
            average_grade = sum(grades) / len(grades)
            max_grade = max(grades)
            file.write(f'{student_name}:{min_grade}, {average_grade:.2f}, {max_grade}\n')
            

student_grades = reading_student_grades('input.txt')
save_accumulated_grades(student_grades , 'output.txt')