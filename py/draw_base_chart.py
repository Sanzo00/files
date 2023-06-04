import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np
from PIL import Image

import scipy.io
import numpy as np
import matplotlib.ticker as mtick



# https://blog.csdn.net/ddpiccolo/article/details/89892449
def plot_line(plot_params, X, Y, labels, xlabel, ylabel, yticks, figpath=None):

  pylab.rcParams.update(plot_params)  #更新自己的设置
  # https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
  # plt.style.use("seaborn-deep")
  # ["seaborn-deep", "grayscale", "bmh", "ggplot"]
  
  # line_styles=['ro-','b^-','gs-','ro--','b^--','gs--']  #线型设置
  # https://matplotlib.org/stable/api/markers_api.html
  makrer_list = ['o', 's', 'v', 'p', '*', 'd', 'X', 'D']
  
  # fig1 = plt.figure(1)
  axes1 = plt.subplot(111)#figure1的子图1为axes1
  for i, (x, y) in enumerate(zip(X, Y)):
    plt.plot(x, y, label = labels[i], marker=makrer_list[i], markersize=5)
  axes1.set_yticks(yticks)

  # axes1 = plt.gca()
  # axes1.grid(True)  # add grid

  plt.legend()
  plt.ylabel(ylabel) 
  plt.xlabel(xlabel) 
  
  figpath = 'plot.pdf' if not figpath else figpath
  plt.savefig(figpath, dpi=1000, bbox_inches='tight', format='pdf')#bbox_inches='tight'会裁掉多余的白边
  print(figpath, 'is plot.')
  plt.close()



def example_line():
  myparams = {
    'axes.labelsize': '10',
    'xtick.labelsize': '10',
    'ytick.labelsize': '10',
    'lines.linewidth': 1,
    'legend.fontsize': '10',
    'font.family': 'Times New Roman',
    'figure.figsize': '4, 3',  #图片尺寸
    'legend.loc': 'lower right', #[]"upper right", "upper left"]
  }

  X = [np.arange(2, 40 + 2, 2), np.arange(2, 40 + 2, 2), np.arange(2, 40 + 2, 2)]
  Y = [
        [0.207,0.198,0.678,0.665,0.78,0.78,0.79,0.783,0.779,0.779,0.786,0.776,0.801,0.788,0.793,0.79,0.786,0.776,0.791,0.8],
        [0.241,0.618,0.588,0.579,0.577,0.614,0.741,0.852,0.903,0.933,0.961,0.974,0.981,0.979,0.984,0.984,0.981,0.98,0.981,0.987],
        [0.001,0.002,0.572,0.568,0.564,0.601,0.587,0.568,0.536,0.58,0.557,0.567,0.601,0.575,0.584,0.559,0.565,0.583,0.58,0.561]
      ]
  yticks = [0.7, 0.9, 0.95, 1.0]
  labels = ['tanh', 'relu', 'sigmoid']
  xlabel = '(a)Iteration:40 '
  ylabel = 'Accuracy'
  
  plot_line(myparams, X, Y, labels, xlabel, ylabel, yticks, 'line.pdf')


def plot_bar(plot_params, Y, labels, xlabel, ylabel, xticks, figpath=None):
  # plt.rcParams.update(plt.rcParamsDefault)
  pylab.rcParams.update(plot_params)  #更新自己的设置
  
  width = 0.15
  color_list = ['b', 'g', 'c', 'r', 'm']
  n = len(labels)
  ind = np.arange(n)                # the x locations for the groups
  for i, y in enumerate(Y):
    plt.bar(ind+width*i,y,width,color=color_list[i], label =labels[i])  
  
  plt.xticks(np.arange(n) + (n/2-0.5)*width, xticks)
  fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
  
  plt.legend()
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)

  # Set the formatter
  axes = plt.gca()   # get current axes
  ticks_fmt = mtick.FormatStrFormatter(fmt)   
  axes.yaxis.set_major_formatter(ticks_fmt) # set % format to ystick.
  axes.grid(True)


  figpath = 'plot.pdf' if not figpath else figpath
  plt.savefig(figpath, dpi=1000, bbox_inches='tight', format='pdf')#bbox_inches='tight'会裁掉多余的白边
  print(figpath, 'is plot.')
  plt.close()



def example_bar():
  params={
    'axes.labelsize': '35',
    'xtick.labelsize':'27',
    'ytick.labelsize':'27',
    'lines.linewidth': 2 ,
    'legend.fontsize': '27',
    'figure.figsize'   : '17, 8',
    'legend.loc': 'best', #[]"upper right", "upper left"]
  }

  Y = [   
        [9.79,7.25,7.24,4.78,4.20],
        [5.88,4.55,4.25,3.78,3.92],
        [4.69,4.04,3.84,3.85,4.0],
        [4.45,3.96,3.82,3.80,3.79],
        [3.82,3.89,3.89,3.78,3.77],
      ]   

  labels = ['m1', 'm2', 'm3', 'm4', 'm5']
  xticks = ('10%','15%','20%','25%','30%')
  xlabel = 'Sample percentage'
  ylabel = 'Error rate'
  plot_bar(params, Y, labels, xlabel, ylabel, xticks, 'bar.pdf')





def plot_stack_bar(plot_params, Y, labels, xlabel, ylabel, xticks, figpath=None):
  plt.rcParams.update(plt.rcParamsDefault)
  pylab.rcParams.update(plot_params)  #更新自己的设置

  width = 0.15
  color_list = ['b', 'g', 'c', 'r', 'm']
  n = len(Y[0])
  ind = np.arange(n)                # the x locations for the groups
  pre_bottom = np.zeros(len(Y[0]))
  for i, y in enumerate(Y):
    # plt.bar(ind+width*i,y,width,color=color_list[i], label =labels[i])  
    plt.bar(ind,y,width,color=color_list[i], label =labels[i], bottom=pre_bottom)
    pre_bottom += y  

  
  # plt.xticks(np.arange(n) + (n/2-0.5)*width, xticks)
  plt.xticks(np.arange(n), xticks)
  fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
  
  # plt.legend(loc="upper right")
  plt.legend()
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)

  # Set the formatter
  axes = plt.gca()   # get current axes
  ticks_fmt = mtick.FormatStrFormatter(fmt)   
  axes.yaxis.set_major_formatter(ticks_fmt) # set % format to ystick.
  axes.grid(True)


  figpath = 'plot.pdf' if not figpath else figpath
  plt.savefig(figpath, dpi=1000, bbox_inches='tight', format='pdf')#bbox_inches='tight'会裁掉多余的白边
  print(figpath, 'is plot.')
  plt.close()




def example_stack_bar():
  params={
    'axes.labelsize': '35',
    'xtick.labelsize':'27',
    'ytick.labelsize':'27',
    'lines.linewidth': 2 ,
    'legend.fontsize': '27',
    'figure.figsize'   : '17, 8',
    'legend.loc': 'best', #[]"upper right", "upper left"]
  }

  Y = [   
        [9.79,7.25,7.24,4.78,4.20],
        [4.69,4.04,3.84,3.85,4.0],
        [4.45,3.96,3.82,3.80,3.79],
        [3.82,3.89,3.89,3.78,3.77],
      ]   

  labels = ['m1', 'm2', 'm3', 'm4']
  xticks = ('10%','15%','20%','25%','30%')
  xlabel = 'Sample percentage'
  ylabel = 'Error rate'
  plot_stack_bar(params, Y, labels, xlabel, ylabel, xticks, 'stack_bar.pdf')


if __name__ == '__main__':
  example_line()
  example_bar()
  example_stack_bar()

  
