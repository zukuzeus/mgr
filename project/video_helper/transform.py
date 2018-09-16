import threading
import time

import shutil
import glob
import numpy as np
import cv2
import os
import random
from tqdm import tqdm
# from .videoconversion import transform_and_save_as_video, convert_frames_to_video, convert_video_to_frames



def convert_video_to_frames(videopath, outputdirpath, transform_image_function=None):
    size = (1920, 1080)
    if not os.path.exists(outputdirpath):
        os.mkdir(outputdirpath)

    cap = cv2.VideoCapture(videopath)
    framesCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    with tqdm(total=framesCount, desc=videopath + " frames to -> " + outputdirpath, ncols=120) as pbar1:
        count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                if transform_image_function is not None:
                    transformed = transform_image_function(frame)
                else:
                    transformed = frame
                transformed = cv2.resize(transformed, size)
                cv2.imwrite(os.path.join(outputdirpath, "frame{:d}.jpg".format(count)), transformed)
            else:
                break
            pbar1.update()
            count += 1
    pbar1.close()
    cap.release()


convert_video_to_frames("C:\\mgr\\drive-download-20180905T195237Z-001\\DSCN9955.MOV",
                        "C:\\mgr\\drive-download-20180905T195237Z-001\\DSCN9955-frames")

str("asdasd").__contains__()






