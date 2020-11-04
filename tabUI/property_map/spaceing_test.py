def show_status_decorator(func):
    # from functools import wraps
    #
    # @wraps(func)
    def decorated(self, *args, **kwargs):
        print(22222222222)
        # self.status_signal.emit('testeststestestets')
        print(self.a)
        func(self, *args, **kwargs)
        print(self.b)
        # self.status_signal.emit('hhhhhhhhh')

    return decorated


# @show_status_decorator
# def adda(a, b):
#     return a+b
#
#
# result = adda(4, 5)


class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @show_status_decorator
    def add(self):
        print('ssdssss')


t = Test(3, 4)
t.add()


