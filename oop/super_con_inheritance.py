# create super inheritance

class Test:
    def __init__(self):
        print("test constructor")

class Demo(Test):
    def __init__(self):
        super().__init__()
        print("demop constructor")

Demo()
