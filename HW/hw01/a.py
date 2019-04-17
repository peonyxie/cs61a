def f(n):
    total = 0
    for i in range (n+1):
        if i%2 == 0:
            total =+ i
    return total

#This function returns the largest factor of N
def factor(n):
    max = 1
    for i in range (2,n):
        if n%i == 0:
            max = i
    return max


def snake(x, y):
    if cake == more_cake:
        return lambda y: x + y
    else:
        return x + y
snake(10, 20)(30)
