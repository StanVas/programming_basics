book_search = input()
book_count = 0
while True:
    book_name = input()
    if book_name == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {book_count} books.')
        break
    if book_search != book_name:
        book_count += 1
    elif book_search == book_name:
        print(f'You checked {book_count} books and found it.')
        break
