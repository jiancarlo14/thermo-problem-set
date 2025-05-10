import numpy as np
import sympy as sp

constants = np.array([
    [13.8594, 2773.78, 220.07],
    [14.0098, 3103.01, 219.79],
    [14.0045, 3279.47, 213.20]
])

temperature = 110 #degC
pressure = 120 #kPa

A, B, C = constants[:, 0], constants[:, 1], constants[:, 2]

Psat = np.e**(A - B/(temperature + C)) #PSAT {1,2,3}
ki = Psat/pressure

for i, p in enumerate(Psat, start=1):
    # print(f"Species {i}: Vapor Pressure = {p:.2f} kPa")
    k = p/pressure
    # print(f"k{i} = {k:.2f}")

V = sp.symbols("V")
z = 1/3
y = []
for i, k in enumerate(ki, start=1):
    exp = (z*k)/(1 + V*(k - 1))
    y.append(exp)
print(y)

expression = y[0] + y[1] + y[2] - 1
d_expression = sp.diff(expression, V)
f = sp.lambdify(V, expression, "numpy")
df = sp.lambdify(V, d_expression, "numpy")

def newton(f, df, x0, tol=1e-6, max=1000) -> float:
    x = x0
    for i in range(max):
        fx = f(x)
        dfx = df(x)

        if abs(fx) < tol:
            print(f"Converged in {i} iterations.")
            return x
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        print(f"Iteration {i + 1}: x = {x}, f(x) = {fx}")

        x = x - fx/dfx

    raise ValueError("Maximum iterations reached. No solutions found.")

V_VALUE = newton(f, df, 0.5)
print(f"V = {V_VALUE:.3f}")
print()
yi = (ki*z)/(1 + V_VALUE*(ki - 1))
print(f"y1 = 1{yi[0]:.3f}, \ny2 = {yi[1]:.3f}, \ny3 = {yi[2]:.3f} ")
x1, x2, x3 = yi*pressure/Psat
print()
print(f"x1 = {x1:.3f}, \nx2 = {x2:.3f}, \nx3 = {x3:.3f} ")
