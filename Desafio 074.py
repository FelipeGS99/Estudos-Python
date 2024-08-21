from random import randint
num1 = randint(0, 99)
num2 = randint(0, 99)
num3 = randint(0, 99)
num4 = randint(0, 99)
num5 = randint(0, 99)
nums = num1, num2, num3, num4, num5
print(nums)
ordem = sorted(nums)
print(f'O maior número é o {ordem[len(nums)-1]} e o menor número é o {ordem[0]}')