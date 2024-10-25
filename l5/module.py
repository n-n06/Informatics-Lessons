def factorial(n : int) -> int:
    '''
    Factorial of a number
    '''
    if n == 0 or n == 1:
        return 1

    return factorial(n - 1) * n
