import math
import cmath

x = [2, math.sqrt(2), 0, -math.sqrt(2), -2, -math.sqrt(2), 0, math.sqrt(2), 0, 0, 0, 0, 0, 0, 0, 0]
c = complex(1, -1)
for k in range(15):
    y = 0
    for n in range(15):
        y += x[n]*cmath.exp(c.imag*k*n*math.pi/8)
    print(y)
