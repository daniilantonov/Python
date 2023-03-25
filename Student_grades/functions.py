import csv
from student import Student


def reading_student_grades(file_path):
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


def save_accumulated_grades(file_path, students):
    with open(file_path, 'w', newline='') as file:
        fieldnames = ['Name', 'Max Grade', 'Min Grade', 'Average Grade', 'Number of Grades']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        csv_writer.writeheader()
        for student in students:
            csv_writer.writerow({
                'Name': student.get_name(),
                'Max Grade': student.get_max_grade(),
                'Min Grade': student.get_min_grade(),
                'Average Grade': student.get_avg_grade(),
                'Number of Grades': student.get_num_grades()
            })
          