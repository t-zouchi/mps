class Nuron:
    def __init__(self):
        self.b = 0
        self.w = []
        self.f = None

    def f2(self, x):
        return x + 2

def func(x):
    return x + 1


def func2(x):
    return x + 2

#インスタンスを生成
n = Nuron()

#インスタンスのfをfuncに設定する
n.f = func
print (n.f(1))

#インスタンスのfをfunc2に設定する
n.f = func2
print (n.f(1))


