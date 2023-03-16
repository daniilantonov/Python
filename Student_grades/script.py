import homework


students = homework.reading_student_grades('grades.csv')
homework.save_accumulated_grades('output.csv', students)
