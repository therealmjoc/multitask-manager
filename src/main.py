import os
import time

name = "Matthew"
tasks = []

class task:
    def __init__(self, taskName, dueDate):
        self.taskName = taskName
        self.dueDate = dueDate

    def __str__(self):
        return f"{self.taskName}({self.dueDate})"


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def homeScreen():
    print(time.time()%24)
    print("Hi "+name+", you have",len(tasks),"tasks due today.")

    print("+------------------------+")
    for task in tasks:
        print("| ",task,"  |")
    print("+------------------------+")

def newTask():
    thisName = input("Task Name: ")
    thisDate = input("Input Date (DD/MM/YY): ")
    thisTask = task(thisName, thisDate)
    tasks.append(thisTask)

def main():
    homeScreen()
    input("Add new task?")
    newTask()
    clearScreen()
    homeScreen()

main()