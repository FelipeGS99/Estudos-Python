listanum = []
num = 0
for c in range(0, 5):
    num = int(input("Digite um número: "))
    if c == 0 or num >= listanum[-1]:
        listanum.append(num)
    else:
        pos = 0
        while pos < len(listanum):
            if num <= listanum[pos]:
                listanum.insert(pos, num)
                break
            pos += 1
print(listanum)
