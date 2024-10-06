class taskPriority:
    def __init__(self):
        self.tasks={}
        
    def getTask(self,task,priority):
        self.tasks[priority]=task
        print(f" Task {task} added with priority {priority} ")
        
    def getPriority(self):
        taskSort=sorted(self.tasks.items())
        for task,priority in taskSort:
            print(f"{task}:{priority}")
def myMain():
    obj=taskPriority()
    while True:
        choice=input("Enter your choice :  ").strip().lower()
        if choice=='add task':
            task=input("Enter the task :  ")
            priority=int(input("Enter task priority :  "))
            obj.getTask(task,priority)
        elif choice=='priority':
            obj.getPriority()
        elif choice=='exit':
            break
        else:
            print("!Invalid Input! \n Please Try Again")
            
myMain()