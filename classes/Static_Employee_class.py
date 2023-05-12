# create Employee class and object

class Employee:
    ''' This is employee class '''
    
    # it's a static variable
    company_code = 1001
    company_name = 'chetu'

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
        
        # it's getting static data 
        print("--------this is static data----------")
        print("company code is ",Employee.company_code)
        print("company name is ", Employee.company_name)
        print()

#make a object
emp1 = Employee(10001,'ashish','baranwal','30000')
emp2 = Employee(10002,'mayur','yerunkar','30')
emp3 = Employee(10003,'alex','jhadhav','50')
emp4 = Employee(10004,'akash','singh','10')

# calling get_data function
emp1.get_data()
emp2.get_data()
emp3.get_data()
emp4.get_data()
