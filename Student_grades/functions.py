import homework


student_grades=homework.reading_student_grades('grades.csv')
homework.save_accumulated_grades(student_grades,'output.csv')
