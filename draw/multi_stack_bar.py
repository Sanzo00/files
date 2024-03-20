import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

def normalized_Y(Y):
  col_sum = Y.sum(axis=0)
  Y = Y / col_sum[np.newaxis, :]
  return Y

def plot_multi_stack_bar(plot_params, my_params, Y1, Y2, labels, xlabel, ylabel, anchor=None, figpath=None):
  # print(plt.rcParams.keys())
    pylab.rcParams.update(plot_params)  #更新自己的设置
    plt.rcParams['pdf.fonttype'] = 42

    width = my_params['bar_width']
    colors = my_params['colors']
    hatchs = my_params['hatchs']

    fig, ax = plt.subplots()
    assert Y1.shape[1] == Y2.shape[1]
    n = Y1.shape[1]
    gap = 0

    ############## stack bar 1
    Y = Y1
    ind = np.arange(n) - width/2 - gap/2              # the x locations for the groups
    pre_bottom = np.zeros(len(Y[0]))
    h_legends = []
    e_legends = []
    for i, y in enumerate(Y):
        leg1 = plt.bar(ind,y,width,color=colors[i],  hatch=hatchs[i], bottom=pre_bottom, linewidth=params['lines.linewidth'], edgecolor='white')
        leg2 = plt.bar(ind, y, width, color='none', bottom=pre_bottom, lw=0.7, edgecolor='black')
        h_legends.append(leg1)
        e_legends.append(leg2)
        pre_bottom += y  

    fontsize = 6
    text_offset = 0.1
    for x,y in zip(ind, Y1[0]):
        plt.text(x-text_offset, 101, "mode1",horizontalalignment='center', verticalalignment='bottom', fontsize=fontsize)
        ax.annotate(f'{y/100:.1%}', xy=(x,-0.55), xytext=(x-.5,-16),arrowprops=dict(arrowstyle="->",color='C3'), color='C3',fontsize=fontsize)


    ############## stack bar 2
    Y = Y2
    ind = np.arange(n) + width/2 + gap/2             # the x locations for the groups
    pre_bottom = np.zeros(len(Y[0]))
    flag = True
    for i, y in enumerate(Y):
        plt.bar(ind,y,width,color=colors[i], hatch=hatchs[i], bottom=pre_bottom, linewidth=params['lines.linewidth'], edgecolor='white')
        plt.bar(ind, y, width, color='none', bottom=pre_bottom, lw=.5, edgecolor='black')
        pre_bottom += y  


    fontsize = 6
    for x,y in zip(ind, Y2[0]):
        plt.text(x+text_offset, 101, "mode2",horizontalalignment='center', verticalalignment='bottom', fontsize=fontsize)
        ax.annotate(f'{y/100:.1%}', xy=(x-.01,0), xytext=(x+.25,+12),arrowprops=dict(arrowstyle="->",color='C3'), color='C3',fontsize=fontsize)


    ax.set_xticks(np.arange(n), xticks, rotation=0)
    ax.tick_params(axis='x', pad=5)
    ax.set_ylim(0, 100)

    legs = [(x,y) for x,y in zip(h_legends, e_legends)]
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
    ax.spines[['right', 'top']].set_visible(False)
    ax.tick_params(bottom=True, left=True) # x,y轴的刻度线

    ax.spines['bottom'].set_linewidth(params['lines.linewidth'])
    ax.spines['left'].set_linewidth(params['lines.linewidth'])
    ax.spines['right'].set_linewidth(params['lines.linewidth'])
    ax.spines['top'].set_linewidth(params['lines.linewidth'])

    figpath = 'plot.pdf' if not figpath else figpath
    plt.savefig(figpath, dpi=1000, bbox_inches='tight', pad_inches=0, format='pdf')
    print(figpath, 'is plot.')
    plt.close()



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


  Y1 = np.random.randint(0, 101, size=(4, 5))
  Y2 = np.random.randint(0, 101, size=(4, 5))

  Y1 = normalized_Y(Y1) * 100
  Y2 = normalized_Y(Y2) * 100

  labels = ['stage1', 'stage2', 'stage3', 'stage4']
  xticks = [f'data{i}' for i in range(5)]
  xlabel = 'Dataset'
  ylabel = 'Norm. Execute Time (%)'

  my_params={
    'ncol': 2, # 图例列数
    'anchor': (0.5, 1.48), # 图例位置
    'columnspacing': 2, # 横向图例间距
    'labelspacing': 0.5, # 纵向图例间距
    'handletextpad': 0.8 , # 文字距离
    'handleheight': 0.7, # 图例高度
    'handlelength': 2, # 图例宽度

    'bar_width': 0.25,
    'colors': ['C0','C1','C2','C3',],
    'hatchs': ['xx','..','**','++'],
  }

  plot_multi_stack_bar(params, my_params, Y1, Y2, labels, xlabel, ylabel, xticks, figpath='multi_stack_bar.pdf')
