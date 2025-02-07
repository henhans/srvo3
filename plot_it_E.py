import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

data = np.loadtxt('it_E_gGA_nb9.dat').T

#fig, ax = plt.subplots()
#ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

plt.plot(np.arange(data.shape[0]),data*13.6057,'b-o')
plt.xlabel('iterations',size=15)
plt.ylabel('E (eV)',size=15)
plt.tight_layout()
plt.show()
