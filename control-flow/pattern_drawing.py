num = int(input("Enter the size of the pattern: "))
row = 0
while row < num:
    for astr in range (0, num):
        print("*", end="")
    print()
    row += 1

