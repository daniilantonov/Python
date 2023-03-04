import script


student_grades=script.reading_student_grades('grades.csv')
script.save_accumulated_grades(student_grades,'output.csv')
