# !python3
import sys
import sympy
from sympy import sympify
from tscore import tscore

"""
USAGE:

Inputs:
    y = f(x1, x2, x3, ..., xn) - function of n independant variables.
    x1, x2, ..., xn - the values of all the independant variables.
    dx1, dx2, ..., dxn - the uncertainty in the values of all the independant
                         variables.
    e.g.
        uncertaintyPropagator.py 'y' 'x1' 'dx1' 'x2' 'dx2'  where y = f(x1, x2)

Outputs:
    dy - the uncertainty in y.
"""
# START HERE - try writing this code to only for for function of 3 variables

# TODO take imputs and assign them to sympy variables y, x1, dx1, ...

eq = sympify('R2*Vin/(R1 + R2)')
x = sympy.symbols('R1')
y = sympy.symbols('R2')
z = sympy.symbols('Vin')

deltax = 0.05
deltay = 0.05
deltaz = 0.055

sol = eq.subs({x: 4.68, y: 4.68, z: 5.055})
print("Expected Vout: %f" % sol)

dx = sympy.diff(eq, x)
dy = sympy.diff(eq, y)
dz = sympy.diff(eq, z)

dx = dx.subs({x: 4.64, y: 4.71, z: 5.055})
dy = dy.subs({x: 4.64, y: 4.71, z: 5.055})
dz = dz.subs({x: 4.64, y: 4.71, z: 5.055})

xEntry = (deltax*dx)**2
yEntry = (deltay*dy)**2
zEntry = (deltaz*dz)**2

B = 2.545
dB = (xEntry + yEntry + zEntry)**0.5
print('uncer', dB)

print('tscore', tscore(2.546, B, 0, dB))
