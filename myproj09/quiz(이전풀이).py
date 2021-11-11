## 새로운 풀이


def myfilter(filter_fn, alter_value):
    def wrap(fn):
        def inner(*args):
            new_args = []
            for arg in args:
                new_args.append(alter_value if filter_fn(arg) else arg)
            return fn(*new_args)

        return inner

    return wrap


"""

alter_value if filter_fn(arg) else arg 
# if 만약에 filter_fn(arg)가 참이라면 왼쪽 alter value 값으로, 
# 아니라면 else arg


"""
