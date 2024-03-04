"""نمودار sin و cos بین صفر تا 2p رسم کرده و ناحیه بین دو منحنی را بصورت هاشور خورده ترسیم کنید."""


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')
plt.fill_between(x, y_sin, y_cos, color='gray', alpha=0.3)

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()
