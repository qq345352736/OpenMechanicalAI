from scipy.integrate import quad

def f(x):
    return x**3

val, err = quad(f, 0, 1)
print(val)   # 0.3333