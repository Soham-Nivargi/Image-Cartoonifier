import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-1,1,100)
x2 = np.linspace(-1,1,100)

X1, X2 = np.meshgrid(x1, x2)

f1 = (x1 + 1)**4 - 9*x1 +2
f2 = (x1 - 1)**4 + 7*x1 +4

#plt.plot(x1, f1, color = 'green')
#plt.plot(x1, f2, color = 'blue')
#plt.show()

f = (X1-X2)**4 + 8*X1*X2 - X1 + X2 + 3

np.reshape(f, X1.shape)

plt.contour(X1,X2,f)
plt.xlabel('X1')
plt.ylabel('X2')

plt.show()


