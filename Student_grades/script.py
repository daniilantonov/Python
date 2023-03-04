import functions


student_grades = functions.reading_student_grades('grades.csv')
functions.save_accumulated_grades(student_grades,'output.csv')
