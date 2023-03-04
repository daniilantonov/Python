import csv
from collections import defaultdict

def reading_student_grades(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        student_grades = defaultdict(list)
        reader = csv.reader(csv_file, delimiter=' ')
        for row in reader:
            if len(row) != 2:
                raise Exception('File structure not valid')
            name = row[0]
            grade_str = row[1]
            try:
                grade = float(grade_str)
            except ValueError:
                raise Exception('Grade must be a number')
            student_grades[name].append(grade)
    return student_grades


def save_accumulated_grades(student_grades, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for student_name, grades in student_grades.items():
            min_grade = min(grades)
            average_grade = sum(grades) / len(grades)
            max_grade = max(grades)
            file.write(f'{student_name}:{min_grade:.2f}, {average_grade:.2f}, {max_grade:.2f}\n')
