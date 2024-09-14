def celsius_to_fahrenheit(Celsius):
    return(Celsius*9/5)+32

def fahrenheit_to_celsius(Fahrenheit):
    return (Fahrenheit-32)*5/9
flag=True
while flag:
    Option=input("Select C for Celsius and F for Fahrenheit: ")
    if Option!="C" and Option!="F":
        print("!!!Invalid Input!!! Please enter 'C' or 'F'.")
    else:
        if Option=="C":
            print("Convert Celsius to Fahrenheit")
            C_temp=float(input("Enter temperature in Celsius: "))
            print("Converted temperature in Fahrenheit:", celsius_to_fahrenheit(C_temp))
        elif Option=="F":
            print("Convert Fahrenheit to Celsius")
            F_temp=float(input("Enter temperature in Fahrenheit: "))
            print("Converted temperature in Celsius:", fahrenheit_to_celsius(F_temp))