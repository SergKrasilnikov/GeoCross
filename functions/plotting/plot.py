import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
from dbfread import DBF
import os.path

def plot_data(z_list_el, xz_list_el, z_list):
    x = np.array(xz_list_el)
    y = np.array(z_list_el)
    fig = plt.figure(figsize=(52, 20))
    plt.plot(x, y)
    for list in z_list:
        plt.plot(xz_list_el, list)

    axes = plt.subplot(1, 1, 1)
    axes.axis([0, 25000, -8000, 1000])
    axes.xaxis.set_major_locator(MultipleLocator(1000.0))
    axes.yaxis.set_major_locator(MultipleLocator(1000.0))
    axes.xaxis.set_minor_locator(MultipleLocator(100.0))
    axes.yaxis.set_minor_locator(MultipleLocator(100.0))
    axes.tick_params(labelsize=20)

    axes.grid(which='major', axis='x', linewidth=1, linestyle='-', color='grey', alpha=0.5)
    axes.grid(which='major', axis='y', linewidth=1, linestyle='-', color='grey', alpha=0.5)
    axes.grid(which='minor', axis='x', linewidth=0.1, linestyle='-', color='grey', alpha=0.5)
    axes.grid(which='minor', axis='y', linewidth=0.1, linestyle='-', color='grey', alpha=0.5)

    plt.savefig(os.path.abspath(f'../geological_crossections/data/output/output.svg'), dpi=500)

    plt.show()