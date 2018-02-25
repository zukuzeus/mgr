import threading
import time

import shutil
import glob
import numpy as np
import cv2
import os
import random
from tqdm import tqdm


# original method
def frames_to_video(inputpath, outputpath, fps):
    image_array = []
    files = [f for f in os.listdir(inputpath) if os.path.isfile(os.path.join(inputpath, f))]
    files.sort(key=lambda x: int(x[5:-4]))
    for i in range(len(files)):
        print("reading file {}".format(files[i]))
        img = cv2.imread(os.path.join(inputpath, files[i]))
        height, width, _ = img.shape
        size = (width, height)
        img = cv2.resize(img, size)
        image_array.append(img)
    fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
    out = cv2.VideoWriter(outputpath, fourcc, fps, size)
    for i in range(len(image_array)):
        print("wrinting frame {} ".format(files[i]))
        out.write(image_array[i])
    out.release()


# detect background and delete it
def background_deletion(img, background_substactor=cv2.createBackgroundSubtractorMOG2()):
    return background_substactor.apply(img)


def convert_frames_to_video(input_dir_path, outputpath):
    fps = 29

    files = [f for f in os.listdir(input_dir_path) if os.path.isfile(os.path.join(input_dir_path, f))]
    files.sort(key=lambda x: int(x[5:-4]))

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    imgForSize = cv2.imread(os.path.join(input_dir_path, files[0]))
    height, width, _ = imgForSize.shape
    size = (width, height)
    # size = (1920, 1080)
    out = cv2.VideoWriter(outputpath, fourcc, fps, size)

    for i in tqdm(range(len(files)), ncols=100, desc="saving to {} video file".format(outputpath)):
        img = cv2.imread(os.path.join(input_dir_path, files[i]))
        height, width, _ = img.shape
        size = (width, height)
        img = cv2.resize(img, size)
        out.write(img)
    out.release()


def convert_video_to_frames(videopath, outputdirpath, transform_image_function=None):
    size = (1280, 720)
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


def transform_and_save_as_video(video, outputfile, transform_image_function=None):
    #     wczytaj obraz
    tempdir = 'tempOpenCv' + str(random.randint(0, 1e10))
    if not os.path.exists(tempdir):
        os.mkdir(tempdir)

    convert_video_to_frames(video, tempdir, transform_image_function)
    convert_frames_to_video(tempdir, outputfile)
    print('video converted {}'.format(outputfile))
    shutil.rmtree(tempdir)


inputpath = 'frames1'
outpath = 'videosmall.avi'
fps = 29
# convert_frames_to_video(inputpath, outpath)

# convert_video_to_frames('DSCN9953.MOV', 'testframesfunc')
# convert_frames_to_video('testframesfunc', outpath)

# transform_and_save_as_video('DSCN9953.MOV', 'videosmall.avi', background_deletion)
# transform_and_save_as_video('DSCN9953.MOV', 'videosmallnone.avi')
movies = os.listdir('resources')


start = time.time()
with tqdm(total=movies.__len__(), ncols=150, position=0, desc='przetwarzanie katalogu z filmami') as pbar2:
    for file in movies:
        print(os.path.splitext(os.path.basename(file))[0] + '_backgroundcut.avi' + ' file save')
        outputfilename = os.path.splitext(os.path.basename(file))[0] + '_backgroundcut.avi'
        transform_and_save_as_video(os.path.join('resources', file), outputfilename, background_deletion)
        pbar2.update()

end = time.time()
print("--- %s seconds ---" % (end - start))