
#### 그 책자 ppt에서

### TODO라고 노란색으로 되어있는데에 바꾸면 됨 ㅋ
### 다른건 안바꿔도 돼

def myfilter(filter_fn, alter_value):
    def wrap(fn):
        def inner(*args):
            # TODO ### 여기만 바꿔서 활용하면 돼 !!!! 
        return inner
    return wrap
# Decorators.py

@myfilter(lambda i: i % 2 == 0, 0)
def mysum(a, b, c, d, e):
    return a + b + c + d + e


@myfilter(lambda i: i % 2 == 0, 1)
def mymultiply(a, b, c, d, e):
    return a * b * c * d * e


print(mysum(1, 2, 3, 4, 5))  # 9
print(mymultiply(1, 2, 3, 4, 5))  # 15

