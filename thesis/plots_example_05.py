import matplotlib.pyplot as plt
import matplotlib.collections as mcol
from matplotlib.legend_handler import HandlerLineCollection, HandlerTuple
from matplotlib.lines import Line2D
from matplotlib import colors 
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pylab as pylab

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap

def u(x,y):
    c1 = np.multiply(1.0-x, 1.0-y)
    s1 = np.multiply(x,y)
    return np.multiply(c1, 1.0-np.exp(s1))


def plot_example05():
    fig = plt.figure(figsize=(12.5,8))
    fig.subplots_adjust(top=0.96,
        bottom=0.035,
        left=0.0,
        right=0.84,
        hspace=0.2,
        wspace=0.2)
    ax = fig.gca(projection='3d')

    # Make data.
    X = np.arange(0.0, 1.05, 0.05)
    Y = np.arange(0.0, 1.05, 0.05)
    X, Y = np.meshgrid(X, Y)
    Z = u(X,Y)

    # Plot the surface.
    #get only part (20-100%) of the gray scale colormap
    cmap = truncate_colormap(cm.gray, 0.0, 0.7)
    surf = ax.plot_surface(X, Y, Z, cmap=cmap, vmin=-0.08, vmax=0.0,
                        linewidth=0, antialiased=True)

    # Customize the z axis.
    ax.set_zlim(-0.08, 0.0)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set_xlabel('X', fontsize=20, labelpad=20)
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylabel('Y', fontsize=20, labelpad=20)
    ax.set_ylim(-0.1, 1.1)
    ax.set_zlabel('Z', fontsize=20, labelpad=17)
    ax.xaxis.set_tick_params(labelsize=18, pad=5)
    ax.yaxis.set_tick_params(labelsize=18, pad=5)
    ax.zaxis.set_tick_params(labelsize=18, pad=5)

    # Add a color bar which maps values to colors.
    cax = fig.add_axes([ax.get_position().x1+0.0018,ax.get_position().y0+0.04,0.04,ax.get_position().height*0.8])


    fig.colorbar(surf, cax=cax, shrink=0.5, aspect=5)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    #plt.tight_layout(pad=0.05)
    plt.savefig('/home/tomhof/stuff/example05.pdf', bbox_inches='tight', pad_inches=0.0, dpi=300)
    plt.show()

def plot_example05_width():
    #EXAMPLE 05

    x = np.arange(10, 110, 10)
    x_major_ticks = x #np.arange(10, 110, 20)
    x_minor_ticks = x

    y_fdm_pint = [0.02426227, 0.00538025, 0.0015, 0.00158608, 0.00117812, 0.000963, 0.000836, 0.000755, 0.0007008, 0.000662]
    y_fdm_dint = [0.02376760, 0.0048800, 0.0013, 0.0010845,   0.00067638, 0.000461, 0.000334, 0.000253, 0.0001988, 0.00016005]

    y_nm_pint = [0.01847452, 0.01052479, 0.010, 0.00992612, 0.01672513, 0.02220043, 0.03104618, 0.03902495, 0.05246783, 0.05246783]

    fig, ax = plt.subplots(figsize=(10,7))

    # note that plot returns a list of lines.  The "l1, = plot" usage
    # extracts the first element of the list into l1 using tuple
    # unpacking.  So l1 is a Line2D instance, not a sequence of lines
    l_fdm_pint, = ax.plot(x, y_fdm_pint,'g--d')
    #l_fdm_dint, = ax.plot(x, y_fdm_dint,'--.')
    l_nm_pint, = ax.plot(x, y_nm_pint,'r--d')
    #l2, l3 = ax.plot(t2, np.sin(2 * np.pi * t2), '--o', t1, np.log(1 + t1), '.')
    #l4, = ax.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 's-.')

    ax.legend((l_fdm_pint, l_nm_pint), ('GPE3C', 'NM'), loc='upper right', shadow=True, fontsize=18)
    ax.set_xlim(10, 100)
    ax.set_xlabel('m=n', fontsize=20)
    ax.set_ylabel('width', fontsize=20)



    ax.set_xticks(x_major_ticks)
    ax.set_xticks(x_minor_ticks, True)

    ax.grid(which='major', color='gray', linestyle='--')
    ax.grid(which='minor', color='gray', linestyle=':')

    #ax.set_title('Szerokość przedziałów wynikowych')
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.show()


def plot_example05_comp_interval():
    #EXAMPLE 05

    x = np.arange(10, 110, 10)
    x_major_ticks = x #np.arange(10, 110, 20)
    x_minor_ticks = x

    y_fdm_pint = [0.02426227, 0.00538025, 0.0015, 0.00158608, 0.00117812, 0.000963, 0.000836, 0.000755, 0.0007008, 0.000662]
    y_fdm_dint = [0.02376760, 0.0048800, 0.0012, 0.0010845,   0.00067638, 0.000461, 0.000334, 0.000253, 0.0001988, 0.00016005]

    dint_up = []
    for (rp, rd) in zip(y_fdm_pint, y_fdm_dint):
        dint_up.append((rp-rd)*100/rp)


    fig, ax = plt.subplots(figsize=(10,7))

    # note that plot returns a list of lines.  The "l1, = plot" usage
    # extracts the first element of the list into l1 using tuple
    # unpacking.  So l1 is a Line2D instance, not a sequence of lines
    l_fdm_pint, = ax.plot(x, dint_up,'g--d')
    #l_nm_pint, = ax.plot(x, y_nm_pint,'r--d')
    #l2, l3 = ax.plot(t2, np.sin(2 * np.pi * t2), '--o', t1, np.log(1 + t1), '.')
    #l4, = ax.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 's-.')

    #ax.legend((l_fdm_pint), ('GPE3C'), loc='upper right', shadow=True)
    ax.set_xlabel('m=n', fontsize=20)
    ax.set_ylabel('[%]', fontsize=20)
    ax.set_xlim(10, 100)


    ax.set_xticks(x_major_ticks)
    ax.set_xticks(x_minor_ticks, True)

    ax.grid(which='major', color='gray', linestyle='--')
    ax.grid(which='minor', color='gray', linestyle=':')

    #ax.set_title('Szerokość przedziałów wynikowych')
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    fig.tight_layout()
    plt.show()


def plot_example05_gpe3c_constans():
    #EXAMPLE 05 GPE3C - CONSTANS

    x = np.arange(10.0, 120, 10)
    x_major_ticks = x #np.arange(10.0, 120, 20)
    x_minor_ticks = x

    p_const = [1.11986, 2.25721, 3.09335, 3.60517, 3.94667, 4.18983, 4.37149, 4.51226, 4.6245, 4.71605, 4.79215]
    lim_p_const = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]

    q_const = [0.706421, 0.889355, 0.941044, 0.962195, 0.973341, 0.980379, 0.985746, 0.989397, 0.992018,  0.994196, 0.996044]
    lim_q_const = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

    r_const = [6.45463, 11.9713, 14.951, 16.7088, 17.8609, 18.6725, 19.2745, 19.7383, 20.1065,  20.4057, 20.6537]
    lim_r_const = [21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0]

    fig, (ax1, ax2, ax3) = plt.subplots(3,1, figsize=(9,11))

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

    ax1.legend((l_lim_p_const,l_p_const ), ('P', 'approx P'), loc='lower right', shadow=True, fontsize=16)
    ax1.set_xlabel('m=n', fontsize=20)
    #ax1.set_ylabel('const P ')
    ax1.set_xticks(x_major_ticks)
    ax1.set_xticks(x_minor_ticks, True)
    ax1.grid(which='major', color='gray', linestyle='--')
    ax1.grid(which='minor', color='gray', linestyle=':')
    ax1.set_xlim(10, 100)
    ax1.tick_params(axis='both', which='major', labelsize=18)
    ax1.tick_params(axis='both', which='minor', labelsize=18)
    #ax1.set_title('const P')


    ax2.set_xticks(x_major_ticks)
    ax2.set_xticks(x_minor_ticks, True)
    ax2.grid(which='major', color='gray', linestyle='--')
    ax2.grid(which='minor', color='gray', linestyle=':')
    #ax2.set_title('const R')
    ax2.legend((l_lim_q_const,l_q_const ), ('Q', 'approx Q'), loc='lower right', shadow=True, fontsize=16)
    ax2.set_xlabel('m=n', fontsize=20)
    ax2.set_xlim(10, 100)
    ax2.tick_params(axis='both', which='major', labelsize=18)
    ax2.tick_params(axis='both', which='minor', labelsize=18)


    ax3.set_xticks(x_major_ticks)
    ax3.set_xticks(x_minor_ticks, True)
    ax3.grid(which='major', color='gray', linestyle='--')
    ax3.grid(which='minor', color='gray', linestyle=':')
    #ax3.set_title('const S')
    ax3.legend((l_lim_r_const,l_r_const ), ('R', 'approx R'), loc='lower right', shadow=True, fontsize=16)
    ax3.set_xlabel('m=n', fontsize=20)
    ax3.set_xlim(10, 100)
    ax2.tick_params(axis='both', which='major', labelsize=18)
    ax2.tick_params(axis='both', which='minor', labelsize=18)

    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)

    fig.tight_layout()
    plt.show()

def main():
    #plot_example05()
    plot_example05_width()
    #plot_example05_comp_interval()
    #plot_example05_gpe3c_constans()

if __name__=="__main__":main()