# Найти сумму трехзначного числа
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

import random
number = int(random.randrange(100, 1000))
print (number)
first = number%10
print (first)
second = (number//10)%10
print (second)
third = int(number/100)
print (third)
sum = first+second+third
print(sum)
