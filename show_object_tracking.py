import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import json
import numpy as np

np.random.seed(0)
colours = np.random.rand(32, 3)
saved_tracks=json.loads(open('saved_tracks.txt','r+').readline())
plt.ion()
fig = plt.figure()
ax1 = fig.add_subplot(111, aspect='equal')
i=0
cap= cv2.VideoCapture('cars.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    image=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    ax1.imshow(image)
    plt.title('Tracked Targets')
    for d in saved_tracks[i]:
    	ax1.add_patch(patches.Rectangle((d[0],d[1]),d[2]-d[0],d[3]-d[1],fill=False,lw=3,ec=colours[d[4]%32,:]))
    fig.canvas.flush_events()
    plt.draw()
    ax1.cla()
    i+=1
