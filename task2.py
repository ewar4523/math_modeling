import matplotlib.pyplot as plt
import numpy as np

def chtoto(a = 1, b = 1, c = 0):
    x = np.arange(-10,10,0.1)
    plt.plot(x, 1/x)

if __name__ == '__main__':
    chtoto()

plt.savefig('file_chutko.png')

