def partial_x(f, x, y, h=1e-5):
    return (f(x+h, y) - f(x-h, y)) / (2*h)

f = lambda x, y: x*x*y + np.sin(y)
print(partial_x(f, 2.0, 0.5))
