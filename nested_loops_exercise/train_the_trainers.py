jury_count = int(input())
presentation = 0
total_grades = 0

while True:
    current_grade = 0
    current_presentation = input()

    if current_presentation == 'Finish':
        total_grades = total_grades / (jury_count * presentation)
        print(f"Student's final assessment is {total_grades:.2f}.")
        break

    presentation += 1

    for grade in range(jury_count):
        member_jury_grade = float(input())
        total_grades += member_jury_grade
        current_grade += member_jury_grade

    current_grade /= jury_count
    print(f'{current_presentation} - {current_grade:.2f}.')
