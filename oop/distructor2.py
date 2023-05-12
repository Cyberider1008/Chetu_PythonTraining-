# import a time
import time

# create a class
class Employee:
    def __init__(self):
        print("......contructor.......")

    #create destructor
    def __del__(self):
        print("......destructor......")

emp1 = Employee()
emp1 = None
time.sleep(8)
print("end of application")
