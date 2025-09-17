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

# Create empty objects for outline and fill
line, = ax.plot([], [], 'r', lw=2)
fill = ax.fill([], [], 'r', alpha=0.3)[0]  # Transparent fill at first

# Animation function
def update(num):
    line.set_data(x[:num], y[:num])
    fill.set_xy(np.column_stack([x[:num], y[:num]]))
    return line, fill

ani = animation.FuncAnimation(fig, update, frames=len(x), interval=20, blit=True)
plt.show()
