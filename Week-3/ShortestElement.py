def shortest(my_list):
    my_list.sort()
    return my_list[0]


def myMain():
    n=int(input("Enter size of the list :  "))
    my_list=[]
    for i in range (n):
        element=int(input("Enter element :  "))
        my_list.append(element)
    shortestEle=shortest(my_list)
    print("Shortest element is :  ",shortestEle)
    
myMain()