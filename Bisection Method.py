# Solving same equation using bisection method
# x^3 - x^2 + 2


def f(x):
    return x * x * x - x * x + 2


# We assumed the initial values
a = -2
b = 3


def bis(a, b):
    if (f(a) * f(b) >= 0):
        print("Wrong Assumption\n")
        return

    c = a
    while ((b - a) >= 0.01):
        # We find the middle point
        c = (a + b) / 2

        if (f(c) == 0.0):
            break
        # Decide the sides to repeat the steps
        if (f(c) * f(a) < 0):
            b = c
        else:
            a = c

    print("The designated root is : ", "%.6f" % c)


bis(a, b)

f = eval()