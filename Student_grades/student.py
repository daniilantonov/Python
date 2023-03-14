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