import numpy as np
import cv2
import os

def frames_to_video(inputpath,outputpath,fps):
   image_array = []
   files = [f for f in os.listdir(inputpath) if os.path.isfile(os.path.join(inputpath, f))]
   files.sort(key = lambda x: int(x[5:-4]))
   for i in range(len(files)):
       img = cv2.imread(inputpath + files[i])
       size =  (img.shape[1],img.shape[0])
       img = cv2.resize(img,size)
       image_array.append(img)
   fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
   out = cv2.VideoWriter(outputpath,fourcc, fps, size)
   for i in range(len(image_array)):
       out.write(image_array[i])
   out.release()

# folder = 'frames1'
# os.mkdir(folder)

cap = cv2.VideoCapture('DSCN9953.MOV')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fgbg = cv2.createBackgroundSubtractorMOG2()
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
# fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('output.avi', fourcc, 29, (1280, 720))
count = 0
while cap.isOpened():
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    if ret == True:
        # frame = cv2.flip(frame, 0)
        print('writing: frame%d.jpg' %count)
        resize = cv2.resize(fgmask, (1280, 720))
        # cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), fgmask)
        # write the flipped frame
        out.write(resize)

        cv2.imshow('frame', resize)
        if cv2.waitKey(10) == 27:  # exit if Escape is hit
            break
    else:
        break
    count += 1


cap.release()
out.release()
cv2.destroyAllWindows()

# inputpath = 'frames'
# outpath =  'frames/video.mp4'
# fps = 29
# frames_to_video(inputpath,outpath,fps)

##wyswietlanie krawędzi
# while(1):
#     ret, frame = cap.read()
#
#     edges = cv2.Canny(frame,100,200)
#
#     cv2.imshow('frame',edges)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()
