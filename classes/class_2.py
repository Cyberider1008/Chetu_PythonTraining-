class Customer:
    def set_name(self, name):
        self.name = name
    def set_id(self, id):
        self.id = id

c = Customer()
c.set_name('ashish')
c.set_id(101)

print(c.name)

