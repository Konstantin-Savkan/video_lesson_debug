from random import randint


def division(divident, divisor):
    return divident/divisor


if __name__ == '__main__':
    while True:
        a = randint(-100, 100)
        b = randint(-10, 10)
        if b != 0:
            result = division(a, b)
        print(result)

