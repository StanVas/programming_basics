bad_grades = int(input())
exercises_count = 0
bad_grades_count = 0
grades = 0
last_exercise = ''
while True:
    exercise = input()
    if exercise == 'Enough':
        print(f'Average score: {grades/exercises_count:.2f}')
        print(f'Number of problems: {exercises_count}')
        print(f'Last problem: {last_exercise}')
        break
    score = int(input())
    exercises_count += 1
    grades += score
    last_exercise = exercise
    if score <= 4:
        bad_grades_count += 1
        if bad_grades == bad_grades_count:
            print(f'You need a break, {bad_grades} poor grades.')
            break
