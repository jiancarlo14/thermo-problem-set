import numpy as np
import sympy as sp
from matplotlib import rc, use
use("TkAgg")
import matplotlib.pyplot as plt

constants = np.array([
    [13.8594, 2773.78, 220.07], # 1
    [14.0045, 3279.47, 213.20], # 2
])

t = sp.symbols("t")
x1 = sp.symbols("x1")
x2 = 1 - x1
p = 90#kPa

def psat_expr(i:int) -> sp.Expr:
    j = i - 1
    A, B, C = constants[j, :]
    psat_expr = np.e**(A - B/(t + C))
    return psat_expr

x1_values = np.linspace(0, 1, 100)
expr = x1*psat_expr(1) + x2*psat_expr(2) - p
d_expr = sp.diff(expr, t)

f = sp.lambdify((x1, t), expr)
df = sp.lambdify((x1, t), d_expr)

def newton_method(f, df, t_INIT, x, toler=1e-6, max_iter=1000):
    iter = 0
    t = t_INIT

    while iter < max_iter:
        iter += 1
        # print(f"Iteration {iter}")
        ft, dft = f(x, t), df(x, t)
        t_new = t - ft/dft
        # print(f"x = {t_new}, f(x) = {ft}")
        # print()
        if abs(ft) <= toler:
            # print(f"t = {t_new} degC")
            return t_new
        else:
            x = t_new

t_values = []
for x in x1_values:
    t = newton_method(f, df, 100, x)
    t_values.append(t)
    # print(t)

print(t_values)
