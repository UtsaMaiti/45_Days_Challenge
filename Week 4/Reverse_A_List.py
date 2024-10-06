def getList(n):
    list=[]
    for i in range(n):
       element = int(input(f"Enter element {i+1}: "))
       list.append(element)
       return list
def reverse(list):
    rev_list=list[::-1]
    return rev_list
def myMain():
    n=int(input(print("Enter the range of list :  ")))
    getList(n)
    print("The Entered list is :  ",getList)
    print("Reverse of the list is : ")
    reverseList=reverse()
    print("The reverse of the list is :  ",reverseList)
    
myMain()