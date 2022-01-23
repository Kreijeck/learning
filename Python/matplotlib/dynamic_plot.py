import matplotlib.pyplot as plt
import matplotlib.animation as animation

import time
x = [1,2]
y = [1,4]

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
count = 1

ax1.clear()
ax1.plot(x, y)

while True:
    x.append(count)
    y.append(count*count)
    ax1.clear()
    ax1.plot(x, y)
    count += 1
    plt.show()

#ani = animation.FuncAnimation(fig, animate, interval=1000)