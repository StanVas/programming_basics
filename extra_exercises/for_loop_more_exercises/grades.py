students_count = int(input())
average_grades = 0
top_marks = 0
middle_marks = 0
bad_marks = 0
fail = 0
for grades in range(students_count):
    mark = float(input())
    average_grades += mark
    if mark < 3:
        fail += 1
    elif mark < 4:
        bad_marks += 1
    elif mark < 5:
        middle_marks += 1
    elif mark < 6.01:
        top_marks += 1
print(f'Top students: {(top_marks/students_count)*100:.2f}%')
print(f'Between 4.00 and 4.99: {(middle_marks/students_count)*100:.2f}%')
print(f'Between 3.00 and 3.99: {(bad_marks/students_count)*100:.2f}%')
print(f'Fail: {(fail/students_count)*100:.2f}%')
print(f'Average: {average_grades/students_count:.2f}')
