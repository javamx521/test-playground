"""简单的示例模块：斐波那契数列与质数判断。"""


def fibonacci(n: int) -> int:
    """返回第 n 个斐波那契数（fib(0)=0, fib(1)=1）。"""
    if n < 0:
        raise ValueError("n 必须是非负整数")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_prime(n: int) -> bool:
    """判断 n 是否为质数。"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == "__main__":
    print("fib(10) =", fibonacci(10))
    print("is_prime(17) =", is_prime(17))
