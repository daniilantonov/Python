import homework


students = homework.reading_student_grades('grades.csv')
homework.save_accumulated_grades('output.csv', students)

# student_grades = homework.reading_student_grades('grades.csv')
# homework.save_accumulated_grades(students, 'output.csv')
