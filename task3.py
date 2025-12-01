import matplotlib.pyplot as plt
import numpy as np

def uoy(radius = 10):
    pi = 3.14
    e = 2.71

    k = 23413432
    phi = np.arange(0.1,8*pi,0.00001)
    r = np.sin(k*phi)

    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('file_chutko.png')

uoy()