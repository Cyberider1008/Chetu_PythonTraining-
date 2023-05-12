class Customer:
    def set_name(self, name):
        self.name = name
    def set_id(self, id):
        self.id = id
    
    #get data from set data
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id


c = Customer()
c.set_name('ashish')
c.set_id(101)


print("customer name is", c.get_name())
print("customer id is", c.get_id())

