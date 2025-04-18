class C:
    def __init__(self, C1: str, C2: int):
        self._C1 = C1
        self._C2 = C2

    def get_C1(self):
        return self._C1

    def set_C1(self, C1: str):
        self._C1 = C1

    def get_C2(self):
        return self._C2

    def set_C2(self, C2: int):
        self._C2 = C2

    def MC1(self):
        print("Método MC1")

    def MC2(self):
        print("Método MC2")

    def MC3(self):
        print("Método MC3")

