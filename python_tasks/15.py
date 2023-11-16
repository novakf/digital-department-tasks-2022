class Calculator:
    last = None

    def __init__(self):
        self.hist = []

    def sum(self, a, b):
        res = a + b
        st = f"sum({a}, {b}) == {round(res, 1)}"
        self.hist.append(st)
        self.__class__.last = st
        return res

    def sub(self, a, b):
        res = a - b
        st = f"sub({a}, {b}) == {round(res, 1)}"
        self.hist.append(st)
        self.__class__.last = st
        return res

    def mul(self, a, b):
        res = a * b
        st = f"mul({a}, {b}) == {round(res, 1)}"
        self.hist.append(st)
        self.__class__.last = st
        return res

    def div(self, a, b, mode: bool = False):
        if mode == False:
            res = a / b
        else:
            res = a % b
        st = f"div({a}, {b}) == {round(res, 1)}"
        self.hist.append(st)
        self.__class__.last = st
        return res

    def history(self, n: int):
        try:
            return self.hist[-n]
        except IndexError:
            return None

    @classmethod
    def clear(cls) -> None:
        cls.last = None