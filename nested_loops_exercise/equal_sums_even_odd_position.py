# first_number = int(input())
# second_number = int(input())
# for num in range(first_number, second_number + 1):
#     odd_sum = 0
#     even_sum = 0
#
#     for current_num in range(len(str(num))):
#         if current_num % 2 == 0:
#             even_sum += int(str(num)[current_num])
#         else:
#             odd_sum += int(str(num)[current_num])
#
#     if even_sum == odd_sum:
#         print(num, end=' ')
n1 = int(input())
n2 = int(input())
# enumerate - достъп всеки символ и неговият индекс в думата
for number in range(n1, n2 + 1):
    number_to_str = str(number)
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end=' ')