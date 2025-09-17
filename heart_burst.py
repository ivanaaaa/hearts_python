import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Heart equation
def in_heart(x, y):
    return (x**2 + y**2 - 1)**3 - x**2 * y**3 <= 0

# Generate LOTS of random endpoints inside the heart
np.random.seed(1)
points = []
while len(points) < 2000:  # more points = denser lines
    x, y = np.random.uniform(-1.5, 1.5), np.random.uniform(-1.5, 1.5)
    if in_heart(x, y):
        points.append((x, y))
points = np.array(points)

# Randomize the order for the burst effect
np.random.shuffle(points)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

lines = []

# Animation function: draw one line per frame
def update(frame):
    x, y = points[frame]
    line, = ax.plot([0, x], [0, y], 'r', lw=0.5)  # thinner lines for density
    lines.append(line)
    return lines

ani = animation.FuncAnimation(fig, update, frames=len(points), interval=1, blit=False, repeat=False)
plt.show()
