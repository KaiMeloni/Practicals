try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
print("Finished.")

# 1. If a number is not enter and instead another character a ValueError will occur.

# 2. DivideByZero Error occurs when the denominator is 0 as a fraction can not be divided by 0.

# 3. Could change code to not accept 0 as a valid input and loop until a valid number is input.

