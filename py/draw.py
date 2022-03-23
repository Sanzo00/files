#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

# 可用的字体
# from matplotlib.font_manager import FontManager
# fm = FontManager()
# mat_fonts = set(f.name for f in fm.ttflist)
# print (mat_fonts)

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

width = 0.35

def draw_bar(x_name, y_data, bar_type, colors, xlabel="", ylabel="", ylim_=0):
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  n = len(x_name)
  x = np.arange(0, n)
  plt.xlim(-1, n)
  plt.xticks(x, x_name)
  # plt.xticks(x_name)
  
  axes = plt.gca()

  # axes.set_xlim([xmin,xmax])

  print('ylim ', max(ylim_, np.max(y_data) + 30))
  plt.ylim(-width, max(ylim_, np.max(y_data) + 30))
  
  # plt.yticks(())
  y_num = len(y_data)
  x_offset = -(y_num * width / 2) / 2
  for i, y in enumerate(y_data):
    # print(x+x_offset+i*width, y)
    plt.bar(x+x_offset+i*width, y, label=bar_type[i], alpha=0.9, width=width, facecolor=colors[i], edgecolor='white')
  # plt.legend(loc="upper right")
  plt.legend(loc="best")
  # plt.show()
  

def draw_text(x_name, y_data, offset):
  n = len(x_name)
  x = np.arange(0, n)
  plt.xlim(-1, n)
  # plt.xticks(x)
  plt.ylim(0, np.max(y_data) + 10)
  # plt.yticks(())
  y_num = len(y_data)
  x_offset = -(y_num * width / 2)
  for i, y in enumerate(y_data):
    for _x, _y in zip(x, y):
      # print(_x+x_offset+i*width, _y)
      plt.text(_x+x_offset+(i+0.5)*width, _y + offset, '%.2f' % _y, ha='center', va='top')
  # plt.show()  

def draw_galois_nts():
  x_name = ['cora', 'citeeseer', 'pubmed']
  galois_time = [21.8215, 64.1638, 59.1279]
  nts_time = [11.3339, 33.2267, 32.8832]
  bar_type = ['Galois-gcn', 'Neutronstar']
  colors = ['#ff9999', '#9999ff', '#ff9999']
  # xlabel = "dataset"
  ylabel = "time (s)"
  draw_bar(x_name, (galois_time, nts_time), bar_type, colors, ylabel=ylabel)
  draw_text(x_name, (galois_time, nts_time), 3)
  # plt.title('run time in 200 epoch (1host 16cpu 32G)')
  plt.title('带通信线程 (200 epoch, 16cpu 32G)')
  plt.show()

def draw_galois_without_thread_nts():
  x_name = ['cora', 'citeeseer', 'pubmed']
  galois_time = [10.8554, 32.4182, 31.6795]
  nts_time = [11.3339, 33.2267, 32.8832]
  bar_type = ['Galois-gcn', 'Neutronstar']
  colors = ['#ff9999', '#9999ff', '#ff9999']
  # xlabel = "dataset"
  ylabel = "time (s)"
  draw_bar(x_name, (galois_time, nts_time), bar_type, colors, ylabel=ylabel)
  draw_text(x_name, (galois_time, nts_time), 2)
  plt.title('不带通信线程 (200 epoch, 16cpu 32G)')
  plt.show()


def draw_distribution():
  x_name = ['2', '4', '8']
  compute_time = [42.5262, 20.3295, 10.092]
  commucation_time = [5.81438, 4.98458, 3.74563]
  bar_type = ['compute', 'comm']
  colors = ['#9999ff', '#ff9999']
  xlabel = "host num"
  ylabel = "time (s)"
  draw_bar(x_name, (compute_time, commucation_time), bar_type, colors, xlabel, ylabel)
  draw_text(x_name, (compute_time, commucation_time), 2)
  plt.title('compute and comm time cost one epoch (16cpu 32G reddit)')
  plt.show()

def draw_distribution2():
  x_name = ['reddit', 'wiki']
  compute_time_8 = [10.6602, -1]
  commucation_time_8 = [4.10859, -1]
  compute_time_16 = [10.6602, -1]
  commucation_time_16 = [4.10859, -1]
  bar_type = ['compute', 'comm']
  colors = ['#9999ff', '#ff9999', '#ff9999']
  xlabel = "host num"
  ylabel = "time (s)"
  draw_bar(x_name, (compute_time8, commucation_time16), bar_type, colors, xlabel, ylabel)
  # draw_text(x_name, (compute_time, commucation_time), 2)
  plt.title('compute and comm time cost one epoch\n(16cpu 32G reddit)')
  plt.show()


def draw_galois_nts_reddit():
  x_name = ['总时间', '通信', '计算']
  # galois_time = [28.9585, 18.0548, 10.9037]
  # nts_time = [6.52166, 3.6801, 2.84156]
  galois_time = [28.95, 18.05, 10.90]
  nts_time = [6.52, 3.68, 2.84]
  bar_type = ['Galois-gcn', 'Neutronstar']
  colors = ['#ff9999', '#9999ff', '#ff9999']
  # xlabel = "dataset"
  ylabel = "time (s)"
  draw_bar(x_name, (galois_time, nts_time), bar_type, colors, "", ylabel)
  draw_text(x_name, (galois_time, nts_time), 1.5)
  plt.title('reedit 数据集 (5 epoch, 8 host 16cpu 32G)')
  plt.show()


def draw_galois_nts_wiki():
  x_name = ['总时间', '通信', '计算']
  galois_time = [750.661, 608.571, 121.2]
  nts_time = [239.263, 144.451, 94.8119]
  bar_type = ['Galois-gcn', 'Neutronstar']
  colors = ['#ff9999', '#9999ff', '#ff9999']
  # xlabel = "dataset"
  ylabel = "time (s)"
  draw_bar(x_name, (galois_time, nts_time), bar_type, colors, "", ylabel, 800)
  draw_text(x_name, (galois_time, nts_time), -3)
  plt.title('wiki数据集 (5 epoch, 16 host 32cpu 64G)')
  plt.show()

def draw_distribution3():
  x_name = ['reddit','wiki']
  galois_time = [750.661, 608.571, 121.2]
  nts_time = [239.263, 144.451, 94.8119]
  bar_type = ['Galois-gcn', 'Neutronstar']
  colors = ['#ff9999', '#9999ff', '#ff9999']
  # xlabel = "dataset"
  ylabel = "time (s)"
  draw_bar(x_name, (galois_time, nts_time), bar_type, colors, "", ylabel, 800)
  draw_text(x_name, (galois_time, nts_time), -3)
  plt.title('wiki数据集 (5 epoch, 16 host 32cpu 64G)')
  plt.show()  

def draw_galois_distribute_without_thread_reddit():
  x_name = ['2 host', '4 host', '8 host']
  galois_time = [(101.065 + 93.248 + 97.6351 + 93.0066) / 4, (49.3042 + 50.9321) / 2, 28.7417]
  galois_time_without_thread = [(90.1114 + 84.9663 + 86.845 + 86.4947) / 4, (42.2243 + 40.9319 + 41.7717) / 3, 24.2487]
  bar_type = ['Galois-gcn', 'Galois-gcn(thread)']
  colors = ['#ff9999', '#9999ff', '#ff9999']
  # xlabel = "dataset"
  ylabel = "time (s)"
  draw_bar(x_name, (galois_time, galois_time_without_thread), bar_type, colors, "", ylabel, 800)
  draw_text(x_name, (galois_time, galois_time_without_thread), 3)
  plt.title('reddit数据集 (5 epoch, 16cpu 32G)')
  plt.show()  

def draw_galois_distribute_without_thread_reddit_nts():
  x_name = ['2 host', '4 host', '8 host']
  galois_time_without_thread = [(90.1114 + 84.9663 + 86.845 + 86.4947) / 4, (42.2243 + 40.9319 + 41.7717) / 3, 24.2487]
  nts_time = [26.7816, 14.1311, 10.1574]
  bar_type = ['Galois-gcn(thread)', 'nts']
  colors = ['#ff9999', '#9999ff', '#ff9999']
  # xlabel = "dataset"
  ylabel = "time (s)"
  draw_bar(x_name, (galois_time_without_thread, nts_time), bar_type, colors, "", ylabel, 800)
  draw_text(x_name, (galois_time_without_thread, nts_time), 3)
  plt.title('reddit数据集 (5 epoch, 16cpu 32G)')
  plt.show() 

def draw_galois_distribute_without_thread_wiki():
  x_name = ['总时间', '通信', '计算']
  galois_time = [727.064, 606.612, 120.564]
  galois_time_without_thread = [504.324, 407.497, 89.4414]
  bar_type = ['Galois-gcn', 'Galois-gcn(thread)']
  colors = ['#ff9999', '#9999ff', '#ff9999']
  ylabel = "time (s)"
  draw_bar(x_name, (galois_time, galois_time_without_thread), bar_type, colors, "", ylabel, 800)
  draw_text(x_name, (galois_time, galois_time_without_thread), 10)
  plt.title('wiki数据集 (5 epoch, 16 host 32cpu 64G)')
  plt.show()  


def draw_nts_distribute_nooverlap():
  x_name = ['wiki(20 epoch)', 'reddit(100 epoch)']
  overlap = [886.742417, 124.123602]
  nooverlap = [994.818643, 141.477570]
  bar_type = ['overlap', 'no-overlap']
  colors = ['#ff9999', '#9999ff', '#ff9999']
  ylabel = "time (s)"
  draw_bar(x_name, (overlap, nooverlap), bar_type, colors, "", ylabel, 800)
  draw_text(x_name, (overlap, nooverlap), 10)
  plt.title('overlap vs no-overlap (16 host 32cpu 64G)')
  plt.show()  

# draw_galois_nts()
# draw_galois_without_thread_nts()
# draw_galois_nts_reddit()
# draw_galois_nts_wiki()

# draw_galois_distribute_without_thread_reddit()
# draw_galois_distribute_without_thread_reddit_nts()
# draw_galois_distribute_without_thread_wiki()

draw_nts_distribute_nooverlap()


# draw_distribution3()
# draw_distribution2()




