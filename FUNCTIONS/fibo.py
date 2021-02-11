def fib(n):
    if n >= 3:
        return fib(n-1) + fib(n-2)
    return 1

print(fib(10))


def fbnc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fbnc(n-1) + fbnc(n-2)

print(fbnc(10))



def fibo(num):
    a = 0
    b = 1
    for i in range(num):
        a, b = b, a+b
    return a

print(fibo(10))