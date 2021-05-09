import numpy as np
import matplotlib.pyplot as plt

nDay = 1.0*50.0
day = np.arange(0.0, nDay)

x = day*0
y = day*0

x[0] = 2.0**10
y[0] = 2.0

for iDay in range(1, int(nDay)):
    x[iDay] = x[iDay-1]+(99.0*x[iDay-1])/(365.0*20.0) - y[iDay-1]
    y[iDay] = y[iDay-1] + ((x[iDay-1]-y[iDay-1])/x[iDay-1])+5*(y[iDay-1]/(365.0*30.0))
    print(y[iDay-1])

plt.plot(day, x, y)
plt.show()

