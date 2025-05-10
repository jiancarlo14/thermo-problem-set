import numpy as np
import sympy as sp

X1 = sp.symbols("X1")

gamma = np.array([
    np.e**(0.95*(1-X1)**2),
    np.e**(0.95*(X1)**2)
])
f_gamma1, f_gamma2 = sp.lambdify(X1, gamma[0]), sp.lambdify(X1, gamma[1])

x1 = 0.05
x2 = 1 - x1
g1, g2 = f_gamma1(x1), f_gamma2(x1)
# print(f"gamma1 = {g1:.2f}, gamma2 = {g2:.2f}")
p1s, p2s = 79.80, 40.50 #kPa

print("a.")
P = x1*p1s*g1 + x2*p2s*g2
print(f"P = {P:.3f} kPa")

y1 = (x1*p1s*g1)/P
print(f"y1 = {y1:.3f}")
print()

y1 = 0.95
y2 = 1 - y1
P_s = sp.symbols("P")
eq1 = sp.Eq(y1*P_s, X1*(0.95*(1-X1)**2)*p1s)
eq2 = sp.Eq(P_s, X1*(0.95*(1-X1)**2)*p1s + (1-X1)*(0.95*X1**2)*p2s)

solution = sp.solve((eq1, eq2), (P_s, X1))
print("b.")
print(solution)
# print(f"P = {solution[P_s]} kPa")
# print(f"x1 = {solution[X1]}")
