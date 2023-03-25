# import csv
# from student import Student


# def reading_student_grades(file_path):
#     students = []
#     with open(file_path, 'r') as file:
#         csv_reader = csv.reader(file)
#         next(csv_reader)
#         for row in csv_reader:
#             name = row[0]
#             grades = [int(grade) for grade in row[1:] if grade.isdigit()]
#             student = Student(name=name, grades=grades)
#             students.append(student)
#     return students


# def save_accumulated_grades(file_path, students):
#     with open(file_path, 'w', newline='') as file:
#         fieldnames = ['Name', 'Max Grade', 'Min Grade', 'Average Grade', 'Number of Grades']
#         csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        
#         csv_writer.writeheader()
#         for student in students:
#             csv_writer.writerow({
#                 'Name': student.get_name(),
#                 'Max Grade': student.get_max_grade(),
#                 'Min Grade': student.get_min_grade(),
#                 'Average Grade': student.get_avg_grade(),
#                 'Number of Grades': student.get_num_grades()
#             })
import csv
from typing import List
from student import Student, Teacher , People


def read_students(file_path: str) -> List[Student]:
    students = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            name = row[0]
            grades = [int(grade) for grade in row[1:] if grade.isdigit()]
            student = Student(name=name, grades=grades)
            students.append(student)
    return students

def save_grades_summary(file_path: str, people: List[People]):
    with open(file_path, 'w', newline='') as file:
        fieldnames = ['Name', 'Max Grade', 'Min Grade', 'Average Grade', 'Number of Grades']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        csv_writer.writeheader()
        for person in people:
            if isinstance(person, Student):
                csv_writer.writerow({
                    'Name': person.get_name(),
                    'Max Grade': person.get_max_grade(),
                    'Min Grade': person.get_min_grade(),
                    'Average Grade': person.get_avg_grade(),
                    'Number of Grades': person.get_num_grades()
                })
            elif isinstance(person, Teacher):
                csv_writer.writerow({
                    'Name': person.get_name(),
                    'Max Grade': 'N/A',
                    'Min Grade': 'N/A',
                    'Average Grade': 'N/A',
                    'Number of Grades': 'N/A',
                    'Subject': person.get_subject()
                })
        