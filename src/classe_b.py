class B:
    def __init__(self, B1: int, B2: float):
        self._B1 = B1
        self._B2 = B2

    def get_B1(self):
        return self._B1

    def set_B1(self, B1: int):
        self._B1 = B1

    def get_B2(self):
        return self._B2

    def set_B2(self, B2: float):
        self._B2 = B2

    def MB1(self):
        print("Método MB1")

    def MB2(self):
        print("Método MB2")

    def MB3(self):
        print("Método MB3") 

