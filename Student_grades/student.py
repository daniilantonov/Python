# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
        
#     def get_name(self):
#         return self.name

#     def get_grades(self):
#         return self.grades

#     def get_max_grade(self):
#         return max(self.grades)

#     def get_min_grade(self):
#         return min(self.grades)

#     def get_avg_grade(self):
#         return sum(self.grades) / len(self.grades)

#     def get_num_grades(self):
#         return len(self.grades)
class People:
    def __init__(self, name):
        self.name = name
    
    def print_info(self):
        print("Name:", self.name)

class Student(People):
    def __init__(self, name, grades):
        super().__init__(name)
        self.grades = grades
        
    def print_info(self):
        super().print_info()
        print("Grades:", self.grades)
        print("Max grade:", self.get_max_grade())
        print("Min grade:", self.get_min_grade())
        print("Avg grade:", self.get_avg_grade())
        print("Number of grades:", self.get_num_grades())

    def get_max_grade(self):
        return max(self.grades)

    def get_min_grade(self):
        return min(self.grades)

    def get_avg_grade(self):
        return sum(self.grades) / len(self.grades)

    def get_num_grades(self):
        return len(self.grades)
       