import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m = 100
m2 = 100

x = 2
y = 0
x2 = 2
y2 = 0

fig, ax = plt.subplots()

anim_object,anim_object2,anim_object3,anim_object4 = plt.plot([],[],'-',[],[],'-',[],[],'-', [], [], '-')

frames_interval = np.linspace(0, 2*np.pi, 100)

ax.set_xlim(-100, 100)
ax.set_ylim(-50, 50)
ax.axis("equal")


# Vm = -sqrt(m) / r^2

def draw_circle_with_radius(ao, radius, xa, ya):
    t = np.linspace(0,2*np.pi, 1000)
    ao.set_data(
        np.sin(t)*radius + xa,
        np.cos(t)*radius + ya
    )

#  (3/4)m/pi=R³
# 
K = 1000
r = 1
xs = -20
ys = 0

def update(a):
    global m
    global m2
    global x
    R = ((3 / 4) * m / np.pi) ** (1/3)
    global r 
    r = ((xs - x)** 2 + (ys - y)**2) ** 1/2
    V = ((4 * np.pi * R ** 2) / r ** 2) * K
    if (m > 0):
        m = m - V
    x = x + 0.1
    
    draw_circle_with_radius(anim_object, R, x, y)

    global x2, y2, m2
    R2 = ((3 / 4) * m2 / np.pi) ** (1/3)
    r = ((xs - x2)** 2 + (ys - y2)**2) ** 1/2
    V2 = ((4 * np.pi * R2 ** 2) / r ** 2) * K
    if (m2 > 0):
        m2 = m2 - V2
    x2 = x2 - 0.1
    draw_circle_with_radius(anim_object2, R2, x2, y2)
    draw_circle_with_radius(anim_object3, 10, xs, ys)
    draw_circle_with_radius(anim_object4, R2, x2, y2)
    
    return anim_object, anim_object2, anim_object3, anim_object4



ani = FuncAnimation(fig, update, frames = frames_interval, interval=50)

ani.save('animation_1.gif', writer="pillow")