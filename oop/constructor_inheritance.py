# create a constructor inheritance

class Test:
    def __init__(self):
        print("test contructor")

class Demo(Test):
    def __init__(self):
        print("demo contructor")

Demo()
