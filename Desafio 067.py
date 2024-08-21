while True:
    mult = int(input("Deseja ver a tabuada de qual número?: "))
    if mult < 0:
        break
    for c in range (1, 11):
        print(f"{mult} x {c} = {mult * c}")
