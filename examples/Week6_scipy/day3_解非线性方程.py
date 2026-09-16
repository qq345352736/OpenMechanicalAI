from scipy.optimize import root

def eq(x):
    return x**3 - 2*x - 5

sol = root(eq, x0=2.0)
print(sol.x)