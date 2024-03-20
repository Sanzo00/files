import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

def plot_subplot(plot_params, my_params, Y, yticks, ylims, labels, xlabel, ylabel, figpath=None):
  # print(plt.rcParams.keys())
    pylab.rcParams.update(plot_params)  #更新自己的设置
    plt.rcParams['pdf.fonttype'] = 42

    width = my_params['bar_width']
    colors = my_params['colors']
    hatchs = my_params['hatchs']

    ylabel = 'Epoch time (s)'

    def one_ax(ax, Y, xlabel, yticks, ylims):
      ax.set_xticks([])
      ax.set_yticks(yticks)
      ax.set_ylim(*ylims)
      ax.set_ylabel(ylabel, labelpad=3)
      ax.set_title(f'{xlabel}',x=0.5,y=-.3, fontsize=14)

      for i, y in enumerate(Y):
        print(i, y)
        ax.bar(i,y,width,color=colors[i], hatch=hatchs[i], label=labels[i] ,edgecolor='black', lw=my_params['bar_line'])  

      # lines, labels = ax1.get_legend_handles_labels()
      # plt.legend(lines, labels , ncol=6, bbox_to_anchor=(1.78, 1.33), columnspacing=1.4, handletextpad=.2, labelspacing=.1, handlelength=1)
      # plt.legend(ncol=6, bbox_to_anchor=(1.78, 1.33), columnspacing=1.4, handletextpad=.2, labelspacing=.1, handlelength=1)


    for i in range(len(Y)):
      num = f'1{len(Y)}{i+1}'
      ax = plt.subplot(int(num))
      one_ax(ax, Y[i], xlabel[i], yticks[i], ylims[i])

    print(labels)

    plt.legend(labels, ncol=my_params['ncol'],
                bbox_to_anchor=my_params['anchor'],
                columnspacing=my_params['columnspacing'],
                labelspacing=my_params['labelspacing'],
                handletextpad=my_params['handletextpad'],
                handleheight=my_params['handleheight'],
                handlelength=my_params['handlelength'])

    plt.subplots_adjust(wspace=.3, hspace=0)#调整子图间距


    # ax = plt.gca()
    # ax.spines[['right', 'top']].set_visible(True)
    # ax.tick_params(bottom=True, left=False) # x,y轴的刻度线

    # ax.spines['bottom'].set_linewidth(params['lines.linewidth'])
    # ax.spines['left'].set_linewidth(params['lines.linewidth'])
    # ax.spines['right'].set_linewidth(params['lines.linewidth'])
    # ax.spines['top'].set_linewidth(params['lines.linewidth'])

    figpath = 'plot.pdf' if not figpath else figpath
    plt.savefig(figpath, dpi=1000, bbox_inches='tight', pad_inches=0, format='pdf')
    print(figpath, 'is plot.')
    plt.close()



def normalized_Y(Y):
  col_sum = Y.sum(axis=0)
  Y = Y / col_sum[np.newaxis, :]
  return Y


if __name__ == '__main__':
 
  params={
    'axes.labelsize': '11',
    'xtick.labelsize':'11',
    'ytick.labelsize':'11',
    'lines.linewidth': 1,
    'legend.fontsize': '11',
    'figure.figsize' : '8, 1.5',
    'legend.loc': 'upper center', #[]"upper right", "upper left"]
    'legend.frameon': False,
    'font.family': 'Arial',
    'font.serif': 'Arial',
  }

  my_params={
    'ncol': 6, # 图例列数
    'anchor': (-0.5, 1.3), # 图例位置
    'columnspacing': 2, # 横向图例间距
    'labelspacing': 0.5, # 纵向图例间距
    'handletextpad': 0.5 , # 文字距离
    'handleheight': 0.5, # 图例高度
    'handlelength': 1.5, # 图例宽度

    'bar_width': 0.5,
    'bar_line': 0.5,
    'colors': ['C0','C1','C2','C3','C4','C5',],
    'hatchs': ['xx','..','**','++','--','oo'],
  }

  labels = ['part1', 'part2', 'part3', 'part4', 'part5', 'part6']
  xlabel = [f'(i) data{i}' for i in range(3)]
  xlabel = ['(a) data1', '(b) data2', '(c) data3']
  ylabel = 'Run time (s)'

  Y = [[20.05,11.23,9.83,9.73,19.73,20.13],
          [5.6135,2.5836,2.7740,2.7105,5.0, 4.6549],
          [5.1903,2.7366,2.8637,2.8210,3.825,3.9445],
         ]
  yticks = [[0, 7, 14, 21], [0, 3, 6, 9], [0, 3, 6]]
  ylims = [(0, 25), (0, 8), (0, 8)]

  plot_subplot(params, my_params, Y, yticks, ylims, labels, xlabel, ylabel, figpath='subplot_bar.pdf')
