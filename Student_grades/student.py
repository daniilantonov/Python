class People:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Name: {self.name}")

class Student:
    def __init__(self, name, grades):
        self.name = name
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

    def print_info(self):
        print(f"Student name: {self.get_name()}\n"
              f"Grades: {self.get_grades()}\n"
              f"Max grade: {self.get_max_grade()}\n"
              f"Min grade: {self.get_min_grade()}\n"
              f"Average grade: {self.get_avg_grade()}\n"
              f"Number of grades: {self.get_num_grades()}")
