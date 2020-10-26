import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))

plt.xlabel('X')
plt.ylabel('Y')
yticks = np.linspace(0, 1, 11)
plt.yticks(yticks)
plt.text(-10, 1, r'$f(x)\ =\ \frac{1}{1+e^{-x}}$',
         fontdict={'size': 16, 'color': 'b'})

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.plot(x, y)
plt.show()
