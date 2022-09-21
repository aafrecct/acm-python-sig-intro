good_students = [input('Nombre: ') for i in range(3)]
bad_students = [input('Nombre: ') for i in range(3)]

sad_students = good_students + bad_students

print(sad_students)

acm_students = [student for student in sad_students
                if student[0].lower() in ['a', 'c', 'm']]

print(acm_students)
