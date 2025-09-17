import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create heart shape using parametric equations
t = np.linspace(0, 2 * np.pi, 300)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.axis('off')

# Create an empty line that will be updated
line, = ax.plot([], [], 'r', lw=2)

# Animation function
def update(num):
    line.set_data(x[:num], y[:num])
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(x), interval=20, blit=True)
plt.show()
