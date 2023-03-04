import csv
from collections import defaultdict


def reading_student_grades(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        student_grades = defaultdict(list)
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            name = row['student_name']
            grade = int(row['grade'])
            student_grades[name].append(grade)
        return student_grades

def save_accumulated_grades(student_grades, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Student Name', 'Min Grade', 'Average Grade', 'Max Grade', 'Number of Grades']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for student_name, grades in student_grades.items():
            min_grade = min(grades)
            average_grade = sum(grades) / len(grades)
            max_grade = max(grades)
            num_grades = len(grades)
            csv_writer.writerow({'Student Name': student_name, 
                                  'Min Grade': min_grade, 
                                  'Average Grade': f'{average_grade:.2f}', 
                                  'Max Grade': max_grade, 
                                  'Number of Grades': num_grades})
            