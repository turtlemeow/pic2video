#coding:utf-8
import cv2
import os
fps = 10
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
video_writer = cv2.VideoWriter(filename='./.avi', fourcc=fourcc, fps=fps, frameSize=(320,256))
for i in range(0,401):
    p = i
    # print(str(p)+'.png'+'233333')
    if os.path.exists('./2/'+str(p)+'.jpg'):
        img = cv2.imread(filename='./2/'+str(p)+'.jpg')
        cv2.waitKey(100)
        video_writer.write(img)
        print(str(p) + '.jpg' + 'Yes!')
video_writer.release()
