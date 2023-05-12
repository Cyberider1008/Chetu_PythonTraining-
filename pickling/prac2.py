import pickle

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def __str__(self):
        return str(self.eno)+"      "+ str(self.ename)+"     "+str(self.esal)




count = int(input("how many times enter the values: "))
list1 = []
for i in range(count):
    name = input("enter ur name: ")
    sal = int(input("enter yiur sal: "))
    employee = Employee(i+1,name,sal)
    list1.append(employee)

with open("Employee.dat","wb") as f:
    pickle.dump(list1,f)
    print("save object...")



with open("Employee.dat","rb") as f:
   data = pickle.load(f)
   print("Printing Employee Information after unpickling")
   
   for j in data:
       print(j)



