# 8 вариант
# Натуральное число, записанное в десятичной системе счисления, называется сверхпростым, если оно остается простым при
# любой перестановке своих цифр. Определить все сверхпростые числа до n.


from itertools import permutations
from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if (n % i) == 0:
            return 1
    return 0


def primePermutations(n):
    for j in permutations(str(n)):
        b = 0
        for i in range(len(j)):
            b = b * 10 + int(j[i])
        if isPrime(b) == 1:
            return 1
    return 0


n = int(input('Введите число: '))
A = []
c = 1
d = 3
for i in range(2, n):
    if isPrime(i) == 0:
        if primePermutations(i) == 0:
            A.append(i)
            c += 1
    if i == d:
        print(end='.')
        d += 50000
print(A)