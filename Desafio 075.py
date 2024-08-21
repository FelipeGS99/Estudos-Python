num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))
num4 = int(input("Digite outro número: "))
nums = num1, num2, num3, num4
par = 0
dig3 = nums.count(3)
if nums.count(9) > 1:
    print(f'O número 9 apareceu {nums.count(9)} vezes')
elif nums.count(9) == 1:
    print(f'O número 9 apareceu {nums.count(9)} vez')
else:
    print('O número 9 não foi digitado nenhuma vez!')
if nums.count(3) > 0:
    print(f'O número 3 foi digitado pela primeira vez na entrada de número {nums.index(3) + 1}')
else:
    print('O número 3 não foi digitado nenhuma vez!')
for c in range(0, len(nums)):
    if nums[c] % 2 == 0:
        par += 1
if par > 0:
    print('Os números pares digitados foram: ')
    for num in nums:
        if par > 1:
            if num % 2 == 0:
                print(f'{num} --> ', end='')
        elif num % 2 == 0:
            print(num)
else:
    print('Nenhum número par foi digitado!')