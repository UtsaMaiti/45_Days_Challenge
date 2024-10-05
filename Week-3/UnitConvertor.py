class unit:
    def __init__(self):
        self.getLength={'centimetre':0.01, 'metre':1, 'kilometre':1000,'feet':0.3048,'inches':0.0254, 'miles':1609.34}
        self.getWeight={'kilogram':1, 'grams':0.001, 'pounds':0.454,'ounces':0.0283, 'tons':907.2,'quintals':100,'stones':6.35}
    def Length(self,value,fromUnit,toUnit):
        return value*(self.getLength[fromUnit]/self.getLength[toUnit])
    def Weight(self,value,fromUnit,toUnit):
        return value*(self.getWeight[fromUnit]/self.getWeight[toUnit])
    def Temp(self,value,ip,op):
        if ip=='C':
           if op=='F':
               return value * 1.8 + 32
           elif op=='K':
               return value + 273.15
           else:
               return value
        elif ip=='F':
           if op=='C':
               return (value - 32) / 1.8
           elif op== 'K':
               return (value + 459.67) * 5 / 9
           else:
               return value
        elif ip=='K':
           if op=='C':
               return value - 273.15
           elif op=='F':
               return value * 9 / 5 - 459.67
           else:
               return value
        else:
           return

def myMain():
   obj=unit()
   print("UNIT CONVERTER")
   while True:
    choice=input("What do you want to convert ? \n ").strip().lower()
    if choice=='length':
        value=float(input("Enter the value you want to convert :  "))
        fromUnit=input("Convert from :  ").strip().lower()
        toUnit=input("To :  ").strip().lower()
        result=obj.Length(value,fromUnit,toUnit)
        print("Your result is :  ",result)
    elif choice=='weight':
        value=float(input("Enter the value you want to convert :  "))
        fromUnit=input("Convert from :  ").strip().lower()
        toUnit=input("To :  ").strip().lower()
        result=obj.Weight(value,fromUnit,toUnit)
        print("Your result is :  ",result)
    elif choice=='temperature':
        value=float(input("Enter the value you want to convert :  "))
        ip=input("Convert from (C,F or K) :  ").strip().upper()
        op=input("To (C,F or K) :  ").strip().upper()
        if ip in ['C', 'F', 'K'] and op in ['C', 'F', 'K']:
             result=obj.Temp(value,ip,op)
             print("Your result is :  ",result)
        else:
            print("!INVALID!")
    elif choice=='exit':
        print("Exiting")
    else:
        print("!INVALID CHOICE! PLEASE TRY AGAIN \n")
myMain()