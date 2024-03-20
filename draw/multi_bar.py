import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

def plot_multi_bar(plot_params, my_params, Y, labels, xlabel, ylabel, anchor=None, figpath=None):
  # print(plt.rcParams.keys())
    pylab.rcParams.update(plot_params)  #更新自己的设置
    plt.rcParams['pdf.fonttype'] = 42

    width = my_params['bar_width']
    colors = my_params['colors']
    hatchs = my_params['hatchs']

    fig, ax = plt.subplots()

    n = len(Y[0])
    m = len(labels)
    ind = np.arange(n)
    offset = np.arange(m) - m / 2 + 0


    for i, y in enumerate(Y):
      plt.bar(ind+(offset[i]*width),y,width,color=colors[i], hatch=hatchs[i], label=labels[i], edgecolor='black', lw=my_params['bar_line'])


    ax.set_xticks(np.arange(n), xticks, rotation=0)
    ax.tick_params(axis='x', pad=5)
    ax.set_ylim(0, 100)

    plt.legend(labels, ncol=my_params['ncol'],
                bbox_to_anchor=my_params['anchor'],
                columnspacing=my_params['columnspacing'],
                labelspacing=my_params['labelspacing'],
                handletextpad=my_params['handletextpad'],
                handleheight=my_params['handleheight'],
                handlelength=my_params['handlelength'])


    plt.xlabel(xlabel, labelpad=2)
    plt.ylabel(ylabel, labelpad=2)

    # axes = plt.gca()
    ax.spines[['right', 'top']].set_visible(True)
    ax.tick_params(bottom=True, left=True) # x,y轴的刻度线

    ax.spines['bottom'].set_linewidth(params['lines.linewidth'])
    ax.spines['left'].set_linewidth(params['lines.linewidth'])
    ax.spines['right'].set_linewidth(params['lines.linewidth'])
    ax.spines['top'].set_linewidth(params['lines.linewidth'])

    figpath = 'plot.pdf' if not figpath else figpath
    plt.savefig(figpath, dpi=1000, bbox_inches='tight', pad_inches=0, format='pdf')
    print(figpath, 'is plot.')
    plt.close()


def plot_multi_bar_white_hatch(plot_params, my_params, Y, labels, xlabel, ylabel, anchor=None, figpath=None):
  # print(plt.rcParams.keys())
    pylab.rcParams.update(plot_params)  #更新自己的设置
    plt.rcParams['pdf.fonttype'] = 42

    width = my_params['bar_width']
    colors = my_params['colors']
    hatchs = my_params['hatchs']

    fig, ax = plt.subplots()

    n = len(Y[0])
    m = len(labels)
    ind = np.arange(n)
    offset = np.arange(m) - m / 2 + 0


    h_legs, e_legs = [], []
    for i, y in enumerate(Y):
      leg1 = plt.bar(ind+(offset[i]*width),y,width,color=colors[i], hatch=hatchs[i], label=labels[i], edgecolor='white')
      leg2 = plt.bar(ind+(offset[i]*width),y,width,color='none', lw=plot_params['lines.linewidth'], edgecolor='black')

      h_legs.append(leg1)
      e_legs.append(leg2)


    ax.set_xticks(np.arange(n), xticks, rotation=0)
    ax.tick_params(axis='x', pad=5)
    ax.set_ylim(0, 100)

    legs = [(x,y) for x,y in zip(h_legs, e_legs)]
    plt.legend(legs, labels, ncol=my_params['ncol'],
                bbox_to_anchor=my_params['anchor'],
                columnspacing=my_params['columnspacing'],
                labelspacing=my_params['labelspacing'],
                handletextpad=my_params['handletextpad'],
                handleheight=my_params['handleheight'],
                handlelength=my_params['handlelength'])


    plt.xlabel(xlabel, labelpad=2)
    plt.ylabel(ylabel, labelpad=2)

    # axes = plt.gca()
    ax.spines[['right', 'top']].set_visible(True)
    ax.tick_params(bottom=True, left=True) # x,y轴的刻度线

    ax.spines['bottom'].set_linewidth(params['lines.linewidth'])
    ax.spines['left'].set_linewidth(params['lines.linewidth'])
    ax.spines['right'].set_linewidth(params['lines.linewidth'])
    ax.spines['top'].set_linewidth(params['lines.linewidth'])

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
    'figure.figsize' : '4, 2',
    'legend.loc': 'upper center', #[]"upper right", "upper left"]
    'legend.frameon': False,
    'font.family': 'Arial',
    'font.serif': 'Arial',
  }

  my_params={
    'ncol': 4, # 图例列数
    'anchor': (0.5, 1.2), # 图例位置
    'columnspacing': 2, # 横向图例间距
    'labelspacing': 0.5, # 纵向图例间距
    'handletextpad': 0.1 , # 文字距离
    'handleheight': 0.7, # 图例高度
    'handlelength': 1.2, # 图例宽度

    'bar_width': 0.2,
    'bar_line': 0.5,
    'colors': ['C3','C1','C2','C0',],
    'hatchs': ['xx','..','**','++'],
  }

  Y1 = np.random.randint(0, 101, size=(4, 5))
  Y2 = np.random.randint(0, 101, size=(4, 5))

  Y1 = normalized_Y(Y1) * 100
  Y2 = normalized_Y(Y2) * 100

  labels = ['part1', 'part2', 'part3', 'part4']
  xticks = [f'data{i}' for i in range(5)]
  xlabel = 'Dataset'
  ylabel = 'Norm. Execute Time (%)'

  plot_multi_bar(params, my_params, Y1, labels, xlabel, ylabel, xticks, figpath='multi_bar.pdf')

  plot_multi_bar_white_hatch(params, my_params, Y1, labels, xlabel, ylabel, xticks, figpath='multi_bar_white_hatch.pdf')

