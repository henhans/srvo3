import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('EV_gGA_nb9.dat').T

plt.plot(data[0]*0.529177,data[1], 'b-o')
plt.xlabel('V ($\AA$)',size=15)
plt.ylabel('E (eV)',size=15)
plt.tight_layout()
plt.show()
