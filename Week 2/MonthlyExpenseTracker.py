class Expense:
    def __init__(self):
        valid_months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        while True:
            month=input("\nEnter the name of month you want to calculate expenses for: ")
            if month in valid_months:
                self.month=month  
                break
            else:
                print("\nInvalid month name! Please enter a valid month.")
        self.categories=["Food", "House rent or EMI", "Transport", "Insurance", "Entertainment", "Personal expenses", "Miscellaneous"]
        self.expenses={}

    def getExpense(self):
        for category in self.categories:
            while True:
                try:
                    expense=float(input(f"\nEnter your expense for {category}: "))
                    self.expenses[category] = expense
                    break
                except ValueError:
                    print("\nInvalid Input! Enter again.")
                    self.expenses[category] = 0

    def calExpense(self):
        return sum(self.expenses.values())

    def showExpense(self):
        print(f"\nYour monthly expense for {self.month} is:")
        for category, expense in self.expenses.items():
            print(f"\n {category}: Rs.{expense}")
        totalExpense=self.calExpense()
        print(f"\nTotal expense is: Rs.{totalExpense}")

def myMainTest():
    print("Welcome to Monthly Expense Tracker")
    repeat = True
    while repeat:
        obj=Expense()
        obj.getExpense()
        obj.showExpense()

        choice = input("\nDo you want to enter expenses again? (Yes/No): ")
        if choice.lower()!='yes':
            repeat=False
            print("Exiting the program. Thank You!")
            break
        
myMainTest()