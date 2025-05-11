import numpy as np
import sympy as sp
from matplotlib import rc, use
use("TkAgg")
import matplotlib.pyplot as plt

constants = np.array([
    [13.8594, 2773.78, 220.07], # 1
    [14.0045, 3279.47, 213.20], # 2
])

t = 90 #degC
p = 90 #kPa

def psat(i:int, temp=t) -> float:
    '''
    returns the vapor pressure of a species given the temperature and the antoine coefficients
    i(int)      = species number
    temp(float) = system temperature
    ''' 
    j = i - 1
    A, B, C = constants[j,:]
    psat_value = np.e**(A - B/(temp + C))
    return psat_value

x1 = sp.symbols("x1")
x2 = 1 - x1
psat1, psat2 = psat(1), psat(2)
P = x1*psat1 + x2*psat2
f_p = sp.lambdify(x1, P)
y1 = x1*psat(1)/P
f_y1 = sp.lambdify(x1, y1)

x1_values = np.linspace(0, 1, 100)
p_values = f_p(x1_values)
y1_values = f_y1(x1_values)


rc('text', usetex=True)
rc('font', family='serif')
plt.rcParams.update({'font.size': 20})
plt.plot(x1_values, p_values,label=r"$P\, \mathrm{vs.}\, x_1$")
plt.plot(y1_values, p_values,label=r"$P\, \mathrm{vs.}\, y_1$")
plt.xlabel(r"$x_1, \, y_1$")
plt.ylabel(r"$P/\mathrm{kPa}$")
plt.legend()
plt.grid(True)
plt.show()
