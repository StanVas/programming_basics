name = input()
average_grade = 0
grade_counter = 0
bad_grade = 0
bad_grade_condition = False
while grade_counter < 12:
    grade = float(input())

    if grade < 4:
        bad_grade += 1
        if bad_grade > 1:
            bad_grade_condition = True
            grade_counter += 1
            break
    else:
        average_grade += grade
        grade_counter += 1

if bad_grade_condition:
    print(f'{name} has been excluded at {grade_counter} grade')

else:
    average_grade /= grade_counter
    print(f'{name} graduated. Average grade: {average_grade:.2f}')
