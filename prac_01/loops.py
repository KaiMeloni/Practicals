for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Part 'a'
for i in range(1, 101, 10):
    print(i, end=' ')
print()

# Part 'b'
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Part 'c'
stars = int(input("Enter the number of Stars: "))
for i in range(stars):
    print("*", end=' ')
print()

# Part 'd'
for i in range(1, stars + 1):
    print("*" * i)
print()
