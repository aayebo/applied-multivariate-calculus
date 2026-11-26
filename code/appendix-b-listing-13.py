def f(x, y):
    return x*x + x*y + y*y

def L(x, y):
    return 3 + 3*(x-1) + 3*(y-1)

point = (1.1, 0.9)
print("exact:", f(*point), "linear:", L(*point))
print("error:", f(*point) - L(*point))
