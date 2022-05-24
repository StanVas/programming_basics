students = 0
standard = 0
kids = 0

movie_name = input()
while movie_name != 'Finish':
    #print(movie_name)
    places = int(input())
    #print(places)
    people = 0
    for i in range(places):
        #print('We are now at iteration ' + str(i))
        command = input()
        if command == 'student':
            #print('student was selected')
            students += 1
        elif command == 'standard':
            #print('standard was selected')
            standard += 1
        elif command == 'kid':
            #print('kid was selected')
            kids += 1
        elif command == 'End':
            #print('End was selected')
            break

        people += 1
    fulfillment = people / places * 100
    fulfillment_txt = '{:.2f}'.format(fulfillment)
    print(f'{movie_name} - {fulfillment_txt}% full.')

    movie_name = input()

total_tickets = standard + students + kids

percentage_student = students/total_tickets * 100
perc_student_txt = '{:.2f}'.format(percentage_student)

percentage_standard = standard/total_tickets * 100
perc_standard_txt = '{:.2f}'.format(percentage_standard)

percentage_kid = kids/total_tickets * 100
perc_kid_txt = '{:.2f}'.format(percentage_kid)

print(f'Total tickets: {total_tickets}')
print(f'{perc_student_txt}% student tickets.')
print(f'{perc_standard_txt}% standard tickets.')
print(f'{perc_kid_txt}% kids tickets.')
