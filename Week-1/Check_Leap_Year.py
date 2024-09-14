def det_leapyr(n):
    if(n%4==0):
        return True
    elif(n%100==0):
        return True
    elif(n%400==0):
        return True
    else:
        return False
print("(Enter year number to check and 0 to exit)")
flag=True
while flag:
    year_no=int(input("Enter the year you want to check :  "))
    if year_no==0:
        flag=False
    else:       
        leap_year=det_leapyr(year_no)
        if leap_year:
            print("It is a Leap Year !")
        else:     
            print("It is not a leap Year !")