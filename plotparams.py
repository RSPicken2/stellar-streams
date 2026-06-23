from pylab import *
import matplotlib.pyplot as plt


def dark():

    params = {'axes.labelsize': 18,
          'axes.titlesize': 18,
          'font.size': 20,
          'legend.fontsize': 18,
          'xtick.labelsize': 18,
          'ytick.labelsize': 18,
          'text.usetex': True,
          'figure.subplot.left'    : 0.18,
          'figure.subplot.right'   : 0.96  ,
          'figure.subplot.bottom'  : 0.17  ,
          'figure.subplot.top'     : 0.96  ,
          'figure.subplot.wspace'  : 0.  ,
          'figure.subplot.hspace'  : 0.  ,
          #'lines.markersize' : 6,
          #'lines.markeredgewidth'  : 50,
          'lines.linewidth' : 4.0,
          #'text.latex.unicode': True,
          'xtick.direction': 'in',
          'ytick.direction': 'in',
          'xtick.minor.size': 4,
          'xtick.minor.width': 2,
          'ytick.minor.size': 4,
          'ytick.minor.width': 2,
          'xtick.major.size': 7.5,
          'xtick.major.width': 2,
          'ytick.major.size': 7.5,
          'ytick.major.width': 2,
          'xtick.major.pad'  : 8,
          'ytick.major.pad'  : 8,
          'axes.facecolor'   : 'black',
          'grid.color'       : 'white',
          'xtick.color'      : 'white',
          'ytick.color'      : 'white',
          'figure.facecolor' : 'black',
          'figure.edgecolor' : 'white',
          'axes.edgecolor'   : 'white',
          'axes.labelcolor'  : 'white'    
          }

    rc('font', **{'family': 'sans-serif', 'sans-serif': ['sans-serif']})
    #plt.minorticks_on()
    ion() # Turn on interactive plotting
    rcParams.update(params)

    return "Now using the dark theme"

def default():

    params = {'axes.labelsize': 18,
          'axes.titlesize': 18,
          'font.size': 20,
          'legend.fontsize': 18,
          'xtick.labelsize': 18,
          'ytick.labelsize': 18,
          'text.usetex': True,
          'figure.subplot.left'    : 0.18,
          'figure.subplot.right'   : 0.96  ,
          'figure.subplot.bottom'  : 0.17  ,
          'figure.subplot.top'     : 0.96  ,
          'figure.subplot.wspace'  : 0.  ,
          'figure.subplot.hspace'  : 0.  ,
          #'lines.markersize' : 6,
          #'lines.markeredgewidth'  : 50,
          'lines.linewidth' : 4.0,
          #'text.latex.unicode': True,
          'xtick.direction': 'in',
          'ytick.direction': 'in',
          'xtick.minor.size': 4,
          'xtick.minor.width': 2,
          'ytick.minor.size': 4,
          'ytick.minor.width': 2,
          'xtick.major.size': 7.5,
          'xtick.major.width': 2,
          'ytick.major.size': 7.5,
          'ytick.major.width': 2,
          'xtick.major.pad'  : 8,
          'ytick.major.pad'  : 8,
          'axes.facecolor'   : 'white',
          'grid.color'       : 'black',
          #'xtick.color'      : 'black',
          #'ytick.color'      : 'black',
          'figure.facecolor' : 'white',
          'figure.edgecolor' : 'black',
          'axes.edgecolor'   : 'black',
          'axes.labelcolor'  : 'black'    
          }


    #rc('font', family='serif')
    #rc('font', **{'family': 'sans-serif', 'sans-serif': ['Geneva']})
    #plt.minorticks_on()
    #ion() # Turn on interactive plotting                                                               
    rcParams.update(params)

    return "Now using the default theme"
