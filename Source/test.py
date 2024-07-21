class a:
    def __init__(self):
        self.A = 'a'
        self.B = 'b'
        self.C = None
        print("a")
    def test(self):
        print("test")
        self.C = self

A = a()
A.test()