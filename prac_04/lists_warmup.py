# What values do the following expressions have?
# 3, 1, 4, 1, 5, 9, 2

numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0]  # 3
numbers[-1]  # null
numbers[3]  # 1
numbers[:-1]  # everything except last number
numbers[3:4]  # start at 4, stop at 1
5 in numbers  # 9
7 in numbers  # 0
"3" in numbers  #
numbers + [6, 5, 3]  # 3, 1, 4, 1, 5, 9, 2, 6, 5, 3

numbers[0] = "ten"
numbers[-1] = 1
numbers[2:]
9 in numbers + [6, 5, 3]

print(numbers)