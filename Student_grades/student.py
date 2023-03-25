class People:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def print_info(self):
        print(f"Name: {self.get_name()}")

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
        print(f"Student name: {self.get_name()}\n"
              f"Grades: {self.get_grades()}\n"
              f"Max grade: {self.get_max_grade()}\n"
              f"Min grade: {self.get_min_grade()}\n"
              f"Average grade: {self.get_avg_grade()}\n"
              f"Number of grades: {self.get_num_grades()}")

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        
    def get_name(self):
        return self.name
    
    def get_subject(self):
        return self.subject
    
    def print_info(self):
        print(f"Name: {self.get_name()}")
        print(f"Subject: {self.get_subject()}")
