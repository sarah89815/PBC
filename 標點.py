# https://medium.com/用力去愛一個人的話-心也會痛的/默默地學-python-互動式圖像-fb25d462bb7

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
# 16:10

lat = np.array([25.01729187269667, 25.02051200386708]) 
lon = np.array([121.53896859236457, 121.55660372995924])  

x, y = (lon, lat) # transform coordinates 

# try
arr = np.empty((len(x),10,10))
for i in range(len(x)):
    f = np.random.rand(5,5)
    arr[i, 0:5,0:5] = f
    arr[i, 5:,0:5] =np.flipud(f)
    arr[i, 5:,5:] =np.fliplr(np.flipud(f))
    arr[i, 0:5:,5:] = np.fliplr(f)

img = plt.imread("/Users/yuchiaching/Desktop/PBC介面圖壓縮/地圖＋畫框.png") 
fig, ax = plt.subplots(figsize=(16, 10), dpi=70)
ax.imshow(img, extent=[121.52283, 121.55670, 25.00897, 25.02854])

# 不顯示座標軸
plt.axis('off')

line, = ax.plot(x, y, ls="", marker='o', color='#fa4a0c') 

# create the annotations box
# 顯示圖片部分
im = OffsetImage(arr[0,:,:], zoom=5)
xybox=(50, 50)
ab = AnnotationBbox(im, (x[0],y[0]), xybox=xybox, xycoords='data',
        boxcoords="offset points",  pad=0.3,  arrowprops=dict(arrowstyle="->"))

# add it to the axes and make it visible
# 把他放到圖表上
ax.add_artist(ab)
# 轉成可顯示
ab.set_visible(False)


# CopyPaste
# 滑鼠事件
# 游標移到該點位置顯示圖片
def hover(event):
    # if the mouse is over the scatter points
    if line.contains(event)[0]:
        # find out the index within the array from the event
        ind, = line.contains(event)[1]["ind"]
        # get the figure size
        w,h = fig.get_size_inches()*fig.dpi
        ws = (event.x > w/2.)*-1 + (event.x <= w/2.) 
        hs = (event.y > h/2.)*-1 + (event.y <= h/2.)
        # if event occurs in the top or right quadrant of the figure,
        # change the annotation box position relative to mouse.
        ab.xybox = (xybox[0]*ws, xybox[1]*hs)
        # make annotation box visible
        ab.set_visible(True)
        # place it at the position of the hovered scatter point
        ab.xy =(x[ind], y[ind])
        # set the image corresponding to that point
        im.set_data(arr[ind,:,:])
    else:
        #if the mouse is not over a scatter point
        ab.set_visible(False)
    fig.canvas.draw_idle()

fig.canvas.mpl_connect('motion_notify_event', hover)

plt.show()
