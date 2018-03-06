import threading
import time

import shutil
import glob
import numpy as np
import cv2
import os
import random
from tqdm import tqdm


# detect background and delete it
def background_deletion(img, background_substactor=cv2.createBackgroundSubtractorMOG2(detectShadows=False)):
    return background_substactor.apply(img)


def morphological_transform(image, rodzaj=cv2.MORPH_OPEN, kernel=np.ones((7, 7), np.uint8), iterations=3):
    morphed_image = cv2.morphologyEx(image.copy(), rodzaj, kernel, iterations)
    return morphed_image


def to_gray_color_converter(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image


def contours_finder(image):
    _, contours, _ = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours is None:
        return []
    else:
        return contours


def contours_rect_drawer(image, contours):
    color = (243, 20, 255)
    rect_line_size = 2
    image_with_contours = image

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        image_with_contours = cv2.rectangle(image_with_contours, (x, y), (x + w, y + h), color, rect_line_size)
    return image_with_contours


def contours_drawer(image, contours):
    image_with_contours = image
    cv2.drawContours(image_with_contours, contours, -1, (0, 180, 0), 2)
    return image_with_contours


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


def convert_video_to_frames(videopath, outputdirpath, transform_image_function=None, displayTransformedFrames=False):
    # size = (1280, 720)
    if not os.path.exists(outputdirpath):
        os.mkdir(outputdirpath)

    cap = cv2.VideoCapture(videopath)

    width = int(cap.get(3))  # float
    height = int(cap.get(4))  # float
    size = (width, height)

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
                # display converted video
                if displayTransformedFrames:
                    cv2.imshow('frame', transformed)
                    if cv2.waitKey(10) == 27:  # exit if Escape is hit
                        break
            else:
                break
            pbar1.update()
            count += 1
    pbar1.close()
    cap.release()


def transform_and_save_as_video(video, outputfile, transform_image_function=None, deleteFramesAfterTransform=True):
    #     wczytaj obraz
    tempdir = 'tempOpenCv' + str(int(time.time()))
    if not os.path.exists(tempdir):
        os.mkdir(tempdir)

    convert_video_to_frames(video, tempdir, transform_image_function)
    convert_frames_to_video(tempdir, outputfile)
    print('video converted {}'.format(outputfile))
    if deleteFramesAfterTransform:
        shutil.rmtree(tempdir)


inputpath = 'frames1'
outpath = 'videosmall.avi'
fps = 29


# convert_frames_to_video(inputpath, outpath)

# convert_video_to_frames('DSCN9953.MOV', 'testframesfunc')
# convert_frames_to_video('testframesfunc', outpath)

# transform_and_save_as_video('DSCN9953.MOV', 'videosmall.avi', background_deletion)
# transform_and_save_as_video('DSCN9953.MOV', 'videosmallnone.avi')

def convert_videos_in_directory(path_to_directory_string):
    movies = os.listdir(path_to_directory_string)

    results = 'resultsOfConversion'
    if not os.path.exists(results):
        os.mkdir(results)

    start = time.time()
    with tqdm(total=movies.__len__(), ncols=150, position=0, desc='przetwarzanie katalogu z filmami') as pbar2:
        for file in movies:
            print(os.path.splitext(os.path.basename(file))[0] + '_backgroundcut.avi' + ' file save')
            outputfilename = os.path.splitext(os.path.basename(file))[0] + '_backgroundcut.avi'
            transform_and_save_as_video(os.path.join('resources', file), os.path.join(results, outputfilename),
                                        background_deletion)
            pbar2.update()
    end = time.time()
    print("--- %s seconds ---" % (end - start))


# convert_video_to_frames('DSCN9955.MOV', 'testframesfuncshadow', background_deletion)
# transform_and_save_as_video('DSCN9955.MOV', 'DSCN9955_backgroundcutwithshadow.avi', background_deletion, False)
convert_videos_in_directory('resources')
