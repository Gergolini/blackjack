import matplotlib.pyplot as plt
import numpy as np
import os

X = [1,2,3,4,5]
y1 = [2,4,6,8,9]
y2 = [3,5,1,4,2]

c_DIR = os.getcwd()
res_DIR = os.path.join(c_DIR, 'result')
os.mkdir(res_DIR)

plt.figure()
plt.plot(X, y1, 'k-*', linewidth=2, markersize=5, label='Gergo')
plt.plot(X, np.exp(X), 'r--o', linewidth=2, markersize=5, label='exp')
plt.plot(X, np.square(X), 'b.-', linewidth=2, markersize=5, label='square')
# colors: 'k/r/g/b/c/m/y'
# lineshape: '-/--/.-/:/'
# markershape: '^/./o/*'
plt.xlabel('my xlabel')
plt.ylabel('my ylabel')
# plt.ylim([0, 20])
plt.title('my title')
plt.legend()
plt.savefig(os.path.join(res_DIR, 'example.pdf'))
# plt.show()
