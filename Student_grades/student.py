class People:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Name: {self.name}")

class Student(People):
    def __init__(self, name, grades):
        super().__init__(name)
        self.grades = grades
        
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
        print(f"Name: {self.name}, Grades: {self.grades}")
      