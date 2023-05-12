# create Employee class and object

class Employee:
    ''' This is employee class '''
    def __init__(self,id,fname,lname,salary):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.salary = salary
    
    #get all data through self variable
    def get_data(self):
        print("eid is ",self.id)
        print("fname is ",self.fname)
        print("lname is ",self.lname)
        print("salary is ",self.salary)

#make a object
emp = Employee(10001,'ashish','baranwal','30000')
emp.get_data()
