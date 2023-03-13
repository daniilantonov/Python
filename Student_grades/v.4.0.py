import csv
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def set_name(self, name):
        self.name = name

    def set_grades(self, grades):
        self.grades = grades

    def get_name(self):
        return self.name

    def get_grades(self):
        return self.grades

    def get_max_grade(self):
        return max(self.grades)

    def get_min_grade(self):
        return min(self.grades)

    def get_avg_grade(self):
        return sum(self.grades) / len(self.grades)

    def get_num_grades(self):
        return len(self.grades)


def reading_student_grades(file_path):
    students = []
    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split(",")
            name = data[0]
            grades = list(map(int, data[1:]))
            student = Student(name, grades)
            students.append(student)
    return students


def save_accumulated_grades(students, file_path):
    with open(file_path, "w", newline="") as file:
        fieldnames = ["Name", "Max Grade", "Min Grade", "Avg Grade", "Num Grades"]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for student in students:
            csv_writer.writerow(
                {
                    "Name": student.get_name(),
                    "Max Grade": student.get_max_grade(),
                    "Min Grade": student.get_min_grade(),
                    "Avg Grade": student.get_avg_grade(),
                    "Num Grades": student.get_num_grades(),
                }
            )
