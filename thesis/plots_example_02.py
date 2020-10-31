import matplotlib.pyplot as plt
import matplotlib.collections as mcol
from matplotlib.legend_handler import HandlerLineCollection, HandlerTuple
from matplotlib.lines import Line2D
import numpy as np

def plot_example02():
    #EXAMPLE 02

    x = np.arange(0.0, 100, 10)
    x_major_ticks = np.arange(0.0, 100, 20)
    x_minor_ticks = x

    y_fdm_pint = [0.02563997, 0.00668377, 0.0032, 0.00197000, 0.0014087, 0.00110469, 0.00092180, 0.00080332, 0.00072221, 0.00066426]
    y_fdm_dint = [0.02523085, 0.00626779, 0.0032, 0.00155228, 0.0009907, 0.00068664, 0.00050368, 0.00038516, 0.00030402, 0.00024605]

    y_nm_pint = [0.07705311, 0.03847967, 0.0283, 0.01951200, 0.01560932, 0.01301575, 0.01115435, 0.01115435, 0.01115435, 0.01115435]

    fig, ax = plt.subplots()

    # note that plot returns a list of lines.  The "l1, = plot" usage
    # extracts the first element of the list into l1 using tuple
    # unpacking.  So l1 is a Line2D instance, not a sequence of lines
    l_fdm_pint, = ax.plot(x, y_fdm_pint,'g--d')
    #l_fdm_dint, = ax.plot(x, y_fdm_dint,'--.')
    l_nm_pint, = ax.plot(x, y_nm_pint,'r--d')
    #l2, l3 = ax.plot(t2, np.sin(2 * np.pi * t2), '--o', t1, np.log(1 + t1), '.')
    #l4, = ax.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 's-.')

    ax.legend((l_fdm_pint, l_nm_pint), ('GPE3C', 'NM'), loc='upper right', shadow=True)
    ax.set_xlabel('m=n')
    ax.set_ylabel('width')


    ax.set_xticks(x_major_ticks)
    ax.set_xticks(x_minor_ticks, True)

    ax.grid(which='major', color='gray', linestyle='--')
    ax.grid(which='minor', color='gray', linestyle=':')

    #ax.set_title('Szerokość przedziałów wynikowych')
    plt.show()


def plot_example02_comp_interval():
    #EXAMPLE 02

    x = np.arange(0.0, 100, 10)
    x_major_ticks = np.arange(0.0, 100, 20)
    x_minor_ticks = x

    y_fdm_pint = [0.02563997, 0.00668377, 0.0015, 0.00197000, 0.0014087, 0.00110469, 0.00092180, 0.00080332, 0.00072221, 0.00066426]
    y_fdm_dint = [0.02523085, 0.00626779, 0.0013, 0.00155228, 0.0009907, 0.00068664, 0.00050368, 0.00038516, 0.00030402, 0.00024605]

    dint_up = []
    for (rp, rd) in zip(y_fdm_pint, y_fdm_dint):
        dint_up.append((rp-rd)*100/rp)


    fig, ax = plt.subplots()

    # note that plot returns a list of lines.  The "l1, = plot" usage
    # extracts the first element of the list into l1 using tuple
    # unpacking.  So l1 is a Line2D instance, not a sequence of lines
    l_fdm_pint, = ax.plot(x, dint_up,'g--d')
    #l_nm_pint, = ax.plot(x, y_nm_pint,'r--d')
    #l2, l3 = ax.plot(t2, np.sin(2 * np.pi * t2), '--o', t1, np.log(1 + t1), '.')
    #l4, = ax.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 's-.')

    #ax.legend((l_fdm_pint), ('GPE3C'), loc='upper right', shadow=True)
    ax.set_xlabel('m=n')
    ax.set_ylabel('percentage')


    ax.set_xticks(x_major_ticks)
    ax.set_xticks(x_minor_ticks, True)

    ax.grid(which='major', color='gray', linestyle='--')
    ax.grid(which='minor', color='gray', linestyle=':')

    #ax.set_title('Szerokość przedziałów wynikowych')
    plt.show()


def plot_example02_gpe3c_constans():
    #EXAMPLE 02 GPE3C - CONSTANS

    x = np.arange(0.0, 110, 10)
    x_major_ticks = np.arange(0.0, 110, 20)
    x_minor_ticks = x

    p_const = [1.11986, 2.25721, 3.09335, 3.60517, 3.94667, 4.18983, 4.37149, 4.51226, 4.6245, 4.71605, 4.79215]
    lim_p_const = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]

    q_const = [0.706421, 0.889355, 0.941044, 0.962195, 0.973341, 0.980379, 0.985746, 0.989397, 0.992018,  0.994196, 0.996044]
    lim_q_const = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

    r_const = [6.45463, 11.9713, 14.951, 16.7088, 17.8609, 18.6725, 19.2745, 19.7383, 20.1065,  20.4057, 20.6537]
    lim_r_const = [21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0]

    fig, (ax1, ax2, ax3) = plt.subplots(3,1)

    # note that plot returns a list of lines.  The "l1, = plot" usage
    # extracts the first element of the list into l1 using tuple
    # unpacking.  So l1 is a Line2D instance, not a sequence of lines
    l_p_const, = ax1.plot(x, p_const,'g--d')
    l_lim_p_const, = ax1.plot(x, lim_p_const,'r--.')
    #l_fdm_dint, = ax.plot(x, y_fdm_dint,'--.')

    l_q_const, = ax2.plot(x, q_const,'b--d')
    l_lim_q_const, = ax2.plot(x, lim_q_const,'r--.')

    l_r_const, = ax3.plot(x, r_const,'m--d')
    l_lim_r_const, = ax3.plot(x, lim_r_const,'r--.')

    #l2, l3 = ax.plot(t2, np.sin(2 * np.pi * t2), '--o', t1, np.log(1 + t1), '.')
    #l4, = ax.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 's-.')

    ax1.legend((l_lim_p_const,l_p_const ), ('const P', 'estim P'), loc='upper left', shadow=True)
    ax1.set_xlabel('m=n')
    #ax1.set_ylabel('const P ')
    ax1.set_xticks(x_major_ticks)
    ax1.set_xticks(x_minor_ticks, True)
    ax1.grid(which='major', color='gray', linestyle='--')
    ax1.grid(which='minor', color='gray', linestyle=':')
    #ax1.set_title('const P')


    ax2.set_xticks(x_major_ticks)
    ax2.set_xticks(x_minor_ticks, True)
    ax2.grid(which='major', color='gray', linestyle='--')
    ax2.grid(which='minor', color='gray', linestyle=':')
    #ax2.set_title('const R')
    ax2.legend((l_lim_q_const,l_q_const ), ('const Q', 'estim Q'), loc='upper left', shadow=True)
    ax2.set_xlabel('m=n')


    ax3.set_xticks(x_major_ticks)
    ax3.set_xticks(x_minor_ticks, True)
    ax3.grid(which='major', color='gray', linestyle='--')
    ax3.grid(which='minor', color='gray', linestyle=':')
    #ax3.set_title('const S')
    ax3.legend((l_lim_r_const,l_r_const ), ('const R', 'estim R'), loc='upper left', shadow=True)
    ax3.set_xlabel('m=n')

    plt.show()

def main():
    #plot_example01()
    #plot_example01_comp_interval()
    plot_example02_gpe3c_constans()

if __name__=="__main__":main()