import matplotlib.pyplot as plt
import matplotlib.collections as mcol
from matplotlib.legend_handler import HandlerLineCollection, HandlerTuple
from matplotlib.lines import Line2D
import numpy as np

#EXAMPLE 01

x = np.arange(0.0, 100, 10)

y_fdm_pint = [0.02563997, 0.00668377, 0.0032, 0.00197000, 0.0014087, 0.00110469, 0.00092180, 0.00080332, 0.00072221, 0.00066426]
y_fdm_dint = [0.02523085, 0.00626779, 0.0032, 0.00155228, 0.0009907, 0.00068664, 0.00050368, 0.00038516, 0.00030402, 0.00024605]

y_nm_pint = [0.07705311, 0.03847967, 0.0283, 0.01951200, 0.01560932, 0.01301575, 0.01115435, 0.01115435, 0.01115435, 0.01115435]

fig, ax = plt.subplots()

# note that plot returns a list of lines.  The "l1, = plot" usage
# extracts the first element of the list into l1 using tuple
# unpacking.  So l1 is a Line2D instance, not a sequence of lines
l_fdm_pint, = ax.plot(x, y_fdm_pint,'--x')
#l_fdm_dint, = ax.plot(x, y_fdm_dint,'--.')
l_nm_pint, = ax.plot(x, y_nm_pint,'--+')
#l2, l3 = ax.plot(t2, np.sin(2 * np.pi * t2), '--o', t1, np.log(1 + t1), '.')
#l4, = ax.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 's-.')

ax.legend((l_fdm_pint, l_nm_pint), ('GPE3C', 'NM'), loc='upper right', shadow=True)
ax.set_xlabel('m=n')
ax.set_ylabel('width')
#ax.set_title('Szerokość przedziałów wynikowych')
plt.show()
