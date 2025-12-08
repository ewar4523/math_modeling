import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([],[])

frames_interval = np.linspace(0, 12*np.pi, 100)

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)


def update(a):
    t = np.linspace(0,12*np.pi, 10000)
    anim_object.set_data(
        np.sin(t)*(2.71**np.cos(t) - 2 * np.cos(4*t) + np.sin(t/12)**5),
        np.cos(t)*(2.71**np.cos(t) - 2*np.cos(4*t)+np.sin(t/12)**5)
    )

    return anim_object

a = 3
a1 = np.sin(a)

print(a1)

ani = FuncAnimation(fig, update, frames = frames_interval, interval=50)

ani.save('animation_1.gif', writer="pillow")