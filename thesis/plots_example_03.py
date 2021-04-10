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
    s1 = np.sin(np.pi*x)
    s2 = np.sin(np.pi*y)
    return np.multiply(s1, s2)

def f(x,y):
    #-1.0*M_PI*M_PI*x*y*(std::exp(x)*sinXsinY + std::exp(y)*sinXsinY);
    s1 = np.sin(np.pi*x)
    s2 = np.sin(np.pi*y)
    c = -1.0*np.pi*np.pi
    cxy = c*np.multiply(x,y)
    
    sinXsinY = np.multiply(s1,s2)
    ex = np.exp(x)
    ey = np.exp(y)

    p1 = np.multiply(ex,sinXsinY)
    p2 = np.multiply(ey,sinXsinY)
    return np.multiply(cxy, np.add(p1,p2))

def plot_example03f():
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
    Z = f(X,Y)

    # Plot the surface.
    #get only part (20-100%) of the gray scale colormap
    cmap = truncate_colormap(cm.gray, 0.0, 0.8)
    surf = ax.plot_surface(X, Y, Z, cmap=cmap, vmin=-15.1, vmax=2.1,
                        linewidth=0, antialiased=True)

    # Customize the z axis.
    ax.set_zlim(-15.1, 2.0)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.00f'))
    ax.set_xlabel('X', fontsize=20, labelpad=20)
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylabel('Y', fontsize=20, labelpad=20)
    ax.set_ylim(-0.1, 1.1)
    ax.set_zlabel('Z', fontsize=20, labelpad=17)
    ax.xaxis.set_tick_params(labelsize=18, pad=5)
    ax.yaxis.set_tick_params(labelsize=18, pad=5)
    ax.zaxis.set_tick_params(labelsize=18, pad=10)

    # Add a color bar which maps values to colors.
    cax = fig.add_axes([ax.get_position().x1+0.0018,ax.get_position().y0+0.04,0.04,ax.get_position().height*0.8])


    fig.colorbar(surf, cax=cax, shrink=0.5, aspect=5)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    #plt.tight_layout(pad=0.05)
    plt.savefig('/home/tomhof/stuff/example03f.pdf', bbox_inches='tight', pad_inches=0.0, dpi=300)
    plt.show()

def plot_example03():
    fig = plt.figure(figsize=(12.5,8))
    fig.subplots_adjust(top=0.96,
        bottom=0.035,
        left=0.0,
        right=0.84,
        hspace=0.2,
        wspace=0.2)
    ax = fig.gca(projection='3d')

    # Make data.
    X = np.arange(0.0, 2.05, 0.05)
    Y = np.arange(0.0, 2.05, 0.05)
    X, Y = np.meshgrid(X, Y)
    Z = u(X,Y)

    # Plot the surface.
    #get only part (20-100%) of the gray scale colormap
    cmap = truncate_colormap(cm.gray, 0.0, 0.8)
    surf = ax.plot_surface(X, Y, Z, cmap=cmap, vmin=-1.1, vmax=1.1,
                        linewidth=0, antialiased=True)

    # Customize the z axis.
    ax.set_zlim(-1.1, 1.1)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set_xlabel('X', fontsize=20, labelpad=20)
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylabel('Y', fontsize=20, labelpad=20)
    ax.set_ylim(-0.1, 1.1)
    ax.set_zlabel('Z', fontsize=20, labelpad=17)
    ax.xaxis.set_tick_params(labelsize=18, pad=5)
    ax.yaxis.set_tick_params(labelsize=18, pad=5)
    ax.zaxis.set_tick_params(labelsize=18, pad=10)

    # Add a color bar which maps values to colors.
    cax = fig.add_axes([ax.get_position().x1+0.0018,ax.get_position().y0+0.04,0.04,ax.get_position().height*0.8])


    fig.colorbar(surf, cax=cax, shrink=0.5, aspect=5)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    #plt.tight_layout(pad=0.05)
    plt.savefig('/home/tomhof/stuff/example03.pdf', bbox_inches='tight', pad_inches=0.0, dpi=300)
    plt.show()

def plot_example03_width():
    #EXAMPLE 03 - GPE, NE3C, NE5C

    x = np.arange(10, 110, 10)
    x_major_ticks = np.arange(10, 110, 20)
    x_minor_ticks = x


    y_gpe_pint = [0.0238037, 0.0059875, 0.0026642, 0.0014992, 0.0009597, 0.0006665, 0.0004897, 0.0003750, 0.0002963, 0.0002400]   
    y_gpe_dint = [0.0238037, 0.0059875, 0.0026642, 0.0014992, 0.0009597, 0.0006665, 0.0004897, 0.0003750, 0.0002963, 0.0002400]


    y_ne3c_pint = [0.1640787, 0.0291802, 0.0110953, 0.0058391, 0.0036885, 0.0026241, 0.0020280, 0.0016637, 0.0014263, 0.0012635]
    y_ne3c_dint = [0.0982625, 0.0089208, 0.0011227, 0.0003999, 0.0007990, 0.0009058, 0.0009226, 0.0009103, 0.0008893, 0.0008670]
    
    
    y_ne5c_pint = [0.1888769, 0.0400103, 0.0165229, 0.0089171, 0.0055524, 0.0037812, 0.0027377, 0.0020724, 0.0016228, 0.0013047]
    y_ne5c_dint = [0.0140658, 0.0160702, 0.0091145, 0.0056932, 0.0038690, 0.0027940, 0.0021099, 0.0016486, 0.0013232, 0.0010853]
    
    fig, ax = plt.subplots()

    # note that plot returns a list of lines.  The "l1, = plot" usage
    # extracts the first element of the list into l1 using tuple
    # unpacking.  So l1 is a Line2D instance, not a sequence of lines
    l_gpe_pint, = ax.plot(x, y_gpe_pint,'g--p')
    #l_fdm_dint, = ax.plot(x, y_fdm_dint,'--.')
    l_ne3c_pint, = ax.plot(x, y_ne3c_pint,'r--d')
    l_ne3c_dint, = ax.plot(x, y_ne3c_dint,'b--d')
    
    l_ne5c_pint, = ax.plot(x, y_ne5c_pint,'c--s')
    l_ne5c_dint, = ax.plot(x, y_ne5c_dint,'y--s')
    #l2, l3 = ax.plot(t2, np.sin(2 * np.pi * t2), '--o', t1, np.log(1 + t1), '.')
    #l4, = ax.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 's-.')

    ax.legend((l_gpe_pint, l_ne3c_pint, l_ne3c_dint,l_ne5c_pint, l_ne5c_dint), ('GPE', 'NE3C PINT', 'NE3C DINT', 'NE5C PINT', 'NE5C DINT'), loc='upper right', shadow=True, fontsize=20)
    ax.set_xlabel('m=n')
    ax.set_ylabel('width')
    ax.set_xlim(10, 100);


    ax.set_xticks(x_major_ticks)
    ax.set_xticks(x_minor_ticks, True)

    ax.grid(which='major', color='gray', linestyle='--')
    ax.grid(which='minor', color='gray', linestyle=':')

    #ax.set_title('Szerokość przedziałów wynikowych')
    plt.show()


def plot_example03_comp_interval():
    #EXAMPLE 05

    x = np.arange(10, 110, 10)
    x_major_ticks = np.arange(10, 110, 20)
    x_minor_ticks = x

    y_fdm_pint = [0.02426227, 0.00538025, 0.0015, 0.00158608, 0.00117812, 0.000963, 0.000836, 0.000755, 0.0007008, 0.000662]
    y_fdm_dint = [0.02376760, 0.0048800, 0.0012, 0.0010845,   0.00067638, 0.000461, 0.000334, 0.000253, 0.0001988, 0.00016005]

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
    ax.set_xlim(10, 100);


    ax.set_xticks(x_major_ticks)
    ax.set_xticks(x_minor_ticks, True)

    ax.grid(which='major', color='gray', linestyle='--')
    ax.grid(which='minor', color='gray', linestyle=':')

    #ax.set_title('Szerokość przedziałów wynikowych')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.show()


def plot_example03_gpe2nd_constans():
    #EXAMPLE 03 GPE2nd - CONSTANS

    x = np.arange(10.0, 120, 10)
    x_major_ticks = np.arange(10.0, 120, 20)
    x_minor_ticks = x
    
    m=n=10

    m_const = [7.17777, 11.31, 12.8514, 13.6433, 14.1236, 14.4455, 14.6888, 14.8778, 15.0237, 15.1408, 15.2433]
    lim_m_const = [16.27, 16.27, 16.27, 16.27, 16.27, 16.27, 16.27, 16.27, 16.27, 16.27, 16.27]

    fig, ax = plt.subplots(figsize=(11,4))

    # note that plot returns a list of lines.  The "l1, = plot" usage
    # extracts the first element of the list into l1 using tuple
    # unpacking.  So l1 is a Line2D instance, not a sequence of lines
    l_m_const, = ax.plot(x, m_const,'g--d')
    l_lim_m_const, = ax.plot(x, lim_m_const,'r--.')
    #l_fdm_dint, = ax.plot(x, y_fdm_dint,'--.')

    ax.legend((l_lim_m_const,l_m_const ), ('M', 'approx M'), loc='lower right', shadow=True, fontsize=18)
    ax.set_xlabel('m=n', fontsize=20)
    ax.set_ylabel('[x $10^2$]', fontsize=20)
    ax.set_xticks(x_major_ticks)
    ax.set_xticks(x_minor_ticks, True)
    ax.grid(which='major', color='gray', linestyle='--')
    ax.grid(which='minor', color='gray', linestyle=':')
    ax.set_xlim(10, 100)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()

def plot_example03_ne3c_constans():
    #EXAMPLE 03 NE3C - CONSTANS

    x = np.arange(10.0, 120, 10)
    x_major_ticks = np.arange(10.0, 120, 20)
    x_minor_ticks = x


    p_const = [17.9227, 27.5066, 29.4278, 30.1115, 30.4299, 30.6033, 30.72, 30.81, 30.90, 30.95, 30.97]
    lim_p_const = [32.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0]

    q_const = [17.9262, 27.5103, 29.4312, 30.1146, 30.4329, 30.6064, 30.72, 30.81, 30.90, 30.95, 30.97]
    lim_q_const = [32.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0]

    fig, (ax1, ax2) = plt.subplots(2,1, figsize=(11,8))

    # note that plot returns a list of lines.  The "l1, = plot" usage
    # extracts the first element of the list into l1 using tuple
    # unpacking.  So l1 is a Line2D instance, not a sequence of lines
    l_p_const, = ax1.plot(x, p_const,'g--d')
    l_lim_p_const, = ax1.plot(x, lim_p_const,'r--.')
    #l_fdm_dint, = ax.plot(x, y_fdm_dint,'--.')

    l_q_const, = ax2.plot(x, q_const,'b--d')
    l_lim_q_const, = ax2.plot(x, lim_q_const,'r--.')

    #l2, l3 = ax.plot(t2, np.sin(2 * np.pi * t2), '--o', t1, np.log(1 + t1), '.')
    #l4, = ax.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 's-.')

    ax1.legend((l_lim_p_const,l_p_const ), ('P', 'approx P'), loc='lower right', shadow=True, fontsize=20)
    ax1.set_xlabel('m=n', fontsize=20)
    ax1.set_ylabel('', fontsize=20)
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
    ax2.legend((l_lim_q_const,l_q_const ), ('Q', 'approx Q'), loc='lower right', shadow=True, fontsize=20)
    ax2.set_xlabel('m=n', fontsize=20)
    ax2.set_ylabel('', fontsize=20)
    ax2.set_xlim(10, 100)
    ax2.tick_params(axis='both', which='major', labelsize=18)
    ax2.tick_params(axis='both', which='minor', labelsize=18)

    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    fig.tight_layout()
    plt.show()

def main():
    #plot_example03()
    #plot_example03f()
    #plot_example03_ne3c_constans()
    plot_example03_width()
    
    
    #plot_example03_comp_interval()
    #plot_example03_gpe2nd_constans()
    #plot_example03_gpe4th_constans()

if __name__=="__main__":main()
