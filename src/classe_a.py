class A:
    def __init__(self):
        self.A1 = 0
        self.A2 = 0.0

    def get_A1(self):
        return self.A1

    def set_A1(self, value):
        self.A1 = value

    def get_A2(self):
        return self.A2

    def set_A2(self, value):
        self.A2 = value

    def MA1(self):
        print("MA1")

    def MA2(self):
        print("MA2")
    
    def MA3(self):
        print("Alteração a classe A partir do clone") #

    @staticmethod
    def getSoma(a, b):
        return a + b

