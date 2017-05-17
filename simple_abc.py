import abc

class ThisAbstract(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def foo(self):
        pass

    @abc.abstractmethod
    def bar(self):
        pass


class Concrete(ThisAbstract):

    def foo(self):
        pass



a = Concrete()
a.bar()