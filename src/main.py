import os
import time

name = "Matthew"
tasks = []

currentHour = (((time.time())/60)/60)%24 + 1


class task:
    def __init__(self, taskName, dueDate):
        self.taskName = taskName
        self.dueDate = dueDate

    def __str__(self):
        return f"{self.taskName}({self.dueDate})"


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def homeScreen():
    print(currentHour + 1)
    if (currentHour < 12):
        greeting = "Good morning"
    elif(currentHour > 12 and currentHour < 17):
        greeting = "Good afternoon"
    else:
        greeting = "Hi"
    print(greeting+" "+name+", you have",len(tasks),"tasks due today.")

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