import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# 1.
# 8 was the generated number on Line 1,
# the smallest possible generated number could have been 5 and the largest is 20

# 2.
# 3 was the number generated for Line 2, could of being as low as 3 and high as 10 with intervals of 2

# 3.
# 4.667 was the number on Line 3, smallest being 2.5 and largest 5.5

print(random.randrange(1, 100, 1))
