number = int(input("Enter a number: "))

if number > 0:
    print("The number is a positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


first = int(input("Enter first number"))
second = int(input("Enter second number"))
third = int(input("Enter third number"))

if first > second and second > third:
    print("First is the greatest number!")
elif second > first and first > third:
    print("Second is the greatest number!")
else:
    print("Third is the greatest number!")

if first < second and second < third:
    print("First is the smallest number!")
elif second < first and first < third:
    print("Second is the smallest number!")
else:
    print("Third is the smallest number!")
