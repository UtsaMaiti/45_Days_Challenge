def digit_sum(no):
    total = 0
    while no > 0:
        digit = no % 10
        total += digit
        no //= 10
    return total
flag=True
while flag:
    print("(Enter number to find sum OR 'Q' to exit)")
    n = int(input("Enter your number: "))
    if n.upper()=="Q":
        flag = False
    else:
        try:
            print("Sum of digits is = ", digit_sum(n))
        except ValueError:
            print("!!!Invalid input!!!. Please enter a number or 'Q' to quit.")