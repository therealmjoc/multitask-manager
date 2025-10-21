import os
import time
import datetime
from datetime import date

# TODO Source system date to fetch all tasks due in the next seven days
# TODO Fully design task according to spec
# TODO Save tasks to a csv file

name = "Matthew"
tasks = []

currentHour = (((time.time())/60)/60)%24 + 1

x = datetime.date.today()


class task:
    def __init__(self, taskName, dueDate):
        self.taskName = taskName
        self.dueDate = dueDate

    def __str__(self):
        return f"{self.taskName} ({self.dueDate})"


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def homeScreen():
    if (currentHour < 12):
        greeting = "Good morning"
    elif(currentHour > 12 and currentHour < 17):
        greeting = "Good afternoon"
    else:
        greeting = "Hi"
    print(greeting+" "+name+", you have",len(tasks),"tasks due today.")
    printTaskTable()

    print("[1] Add new task    [2] View All Tasks    [3] Settings    [4] Quit")

def printTaskTable():
    print("Your week at a glance:")
    print("+------------------------+")
    for task in tasks:
        print("| ",task)
    print("+------------------------+")

def newTask():
    thisName = input("Task Name: ")
    thisDay = int(input("Input Day:"))
    thisMonth = int(input("Input Month:"))
    thisYear = int(input("Input Year:"))

    thisDate = date(thisYear, thisMonth, thisDay)

    thisTask = task(thisName, thisDate)
    tasks.append(thisTask)

def main():
    homeScreen()
    while True:
        choice = int(input())
        match choice:
            case 1:
                newTask()
            case 4:
                quit()
            case _:
                print("Invalid operation")
        clearScreen()
        homeScreen()

main()