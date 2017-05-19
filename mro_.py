"""
If our goal is to create a subclass with an MRO to our liking, we need to know how it is calculated.
 The basics are simple. The sequence includes the class, its base classes, 
 and the base classes of those bases and so on until reaching object which is the root class of all classes. 
 The sequence is ordered so that a class always appears before its parents, and if there are multiple parents, 
 they keep the same order as the tuple of base classes.
"""

class Z(object):
    pass

class X(object):
    pass

class A_(Z , X):
    pass

class A(A_):
    pass

class M(object):
    pass

class B(A, M):
    pass

class C(dict):
    pass


class ex(B, C):
    pass


# print(ex.__mro__)


class foo(object):
    def say_hello(self):
        print("hello there---foo")

class bar(foo):
    # def say_hello(self):
    #     print("hello there---bar")
    pass

class far(foo):
    def say_hello(self):
        print("hello there---far")

class zoo(bar, far):
    pass

# print(zoo.__mro__)
zoo().say_hello()