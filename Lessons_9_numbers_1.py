print(1/3)                          #числа з плаваючою крапкою
print((2/3) + (1/2))

import decimal                      #імпорт бібліотеки десятизначні числа: фіксована точність
d = decimal.Decimal ('3.141')
print(d + 1)
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

from fractions import Fraction      #Дроби: чисельник + знаменник
f = Fraction(2, 3)
print(f + 1)
print(f + Fraction(1, 2))
