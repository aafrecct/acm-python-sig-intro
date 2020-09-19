good_students = [input('Name: ') for i in range(2)]
bad_students = [input('Name: ') for i in range(6)]

sad_students = good_students + bad_students
acm_students = [student for student in sad_students
                if student[0].lower() in ['a', 'c', 'm']]

print(acm_students)
