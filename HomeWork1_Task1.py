# Вариант 8
# Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?
n1 = 0
while n1 < 1000 or n1 > 9999:
    n1 = int(input('Введите натуральное четырехзначное число: '))
    if n1 < 1000 or n1 > 9999:
        print('Введено неверное число, попробуйте еще раз.')
A = []
n = n1
for i in range(4):
    A.append(n % 10)
    n = n // 10
status = 0
for i in range(4):
    for j in range(4):
        if not (i == j):
            if A[i] == A[j]:
                status = 1
if status == 1:
    print('В числе ' + str(n1) + ' есть одинаковые цифры.')
else:
    print('В числе ' + str(n1) + ' нет одинаковых цифр.')
