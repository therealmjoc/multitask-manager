import os
import time
import datetime
from datetime import date, timedelta

# TODO Source system date to fetch all tasks due in the next seven days
# TODO Fully design task according to spec
# TODO Save tasks to a csv file

name = "Matthew"
tasks = []

currentHour = (((time.time())/60)/60)%24 + 1

today = datetime.date.today()

# Task objects
class task:
    def __init__(self, taskName, category, dueDate):
        self.taskName = taskName
        self.category = category
        self.dueDate = dueDate

    def __str__(self):
        return f"[{self.category}] {self.taskName} ({self.dueDate})"


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def homeScreen():
    if (currentHour < 12):
        greeting = "Good morning"
    elif(currentHour > 12 and currentHour < 17):
        greeting = "Good afternoon"
    elif(currentHour > 17):
        greeting = "Good evening"
    else:
        greeting = "Hi"
    print(greeting+" "+name+", you have",len(fetchTasks(today)),"tasks due today.")
    print("Your week at a glance:")
    printTaskTable(7)

    print("[1] Add new task    [2] View All Tasks    [3] Settings    [4] Quit")

def printTaskTable(daysFromNow):
    fetchedTasks = fetchTasks(today + timedelta(days=daysFromNow))
    print("You have",len(fetchedTasks),"tasks due in the next",daysFromNow,"days")
    print("+------------------------+")
    for task in fetchedTasks:
        print("| ",task)
    print("+------------------------+")

def newTask():
    print("---- Add New Task ----")
    thisName = input("Task Name: ")
    thisCategory = input("Assignment category: ")
    thisDay = int(input("Input Day:"))
    thisMonth = int(input("Input Month:"))
    thisYear = int(input("Input Year:"))

    thisDate = date(thisYear, thisMonth, thisDay)

    thisTask = task(thisName, thisCategory, thisDate)
    tasks.append(thisTask)

# Fetches all tasks that are within the range of dates provided
def fetchTasks(endDate):
    tasksToReturn = []
    for task in tasks:
        if task.dueDate <= endDate:
            tasksToReturn.append(task)
    return tasksToReturn


def main():
    clearScreen()
    homeScreen()
    while True:
        choice = int(input())
        match choice:
            case 1:
                clearScreen()
                newTask()
            case 2:
                clearScreen()
                printTaskTable(9999)
                input("Press any key to continue")
            case 4:
                quit()
            case _:
                print("Invalid operation")
        clearScreen()
        homeScreen()

main()