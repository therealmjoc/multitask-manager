import os
import time

name = "Matthew"
tasks = []

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def homeScreen():
    print(time.time()%24)
    print("Hi "+name+", you have",len(tasks),"tasks due today.")

    print("+------------------------+")
    for i in range (5):
        print("|                        |")
    print("+------------------------+")

def newTask(task):
    tasks.append(task)

def main():
    homeScreen()
    thistask = input()
    newTask(thistask)
    clearScreen()
    homeScreen()
    print(tasks)

main()