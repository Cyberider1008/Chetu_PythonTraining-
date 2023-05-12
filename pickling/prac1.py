import pickle

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def __str__(self):
        return str(self.eno)+" "+str(self.ename)+" "+str(self.esal)



with open("Employee.dat","wb") as f:
    employee = Employee(101,"san",444444)
    pickle.dump(employee,f)
    print("save object...")



with open("Employee.dat","rb") as f:
    employee = pickle.load(f)
    print(employee)
