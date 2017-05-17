class Memoize(object):

    def __init__(self):
        self.res_dict = {}

    def __call__(self, func):

        def wrapper(*args, **kwargs):
            hash_key = self._hash(args, kwargs)
            if hash_key not in self.res_dict:
                res = func(*args, **kwargs)
                self.res_dict[hash_key] = res
                return res

            return self.res_dict[hash_key]

        return wrapper

    @staticmethod
    def _hash(arg, kwarg):
        return str(arg) + str(kwarg)

# usage :-

# @Memoize
# def func():
#   pass


# FASTEST MEMOIZATION  for function with single argument
def Mem(func):

    class Wrapper(dict):

        def __missing__(self, key):
            ret = self[key] = func(key)
            return ret

    return Wrapper().__getitem__