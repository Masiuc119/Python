# Вариант 8
import math

y = 5
t = -7.4
n = 9
j = (0.5, 8.4, 0.3)
print('Цикл for:')
for i in range(len(j)):
    w = (0.6 * j[i]) + math.exp(t * j[i]) * pow((4 * y) / n, 2)
    s = math.sqrt(w - (0.1 * t)) / (2 + pow(n, 2))
    print(s)
print('\nЦикл while:')
j = 0
while j <= 2:
    w = (0.6 * j) + math.exp(t * j) * pow((4 * y) / n, 2)
    s = math.sqrt(w - (0.1 * t)) / (2 + pow(n, 2))
    print(s)
    j += 0.1
print('\nДвойной цикл:')
y = (0.1, -3, 0.5)
for i in range(len(y)):
    j = 0
    print('y = ' + str(y[i]))
    while j <= 0.4:
        w = (0.6 * j) + math.exp(t * j) * pow((4 * y[i]) / n, 2)
        s = math.sqrt(w - (0.1 * t)) / (2 + pow(n, 2))
        print(s)
        j += 0.1
