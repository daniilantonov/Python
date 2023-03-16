import functions


students = functions.reading_student_grades('grades.csv')
functions.save_accumulated_grades('output.csv', students)
