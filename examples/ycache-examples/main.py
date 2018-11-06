from yutil import ycache as cache


@cache
def add(a, b):
    print('function is running')
    return a + b


if __name__ == '__main__':
    print(add(3, 4))
    print(add(3, 4))
    print(add(8, 4))
    print(add(4, 8))
