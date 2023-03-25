import functions


students = functions.read_students('grades.csv')
functions.save_grades_summary('output.csv', students)
