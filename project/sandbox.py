import project.simpleDetecting as sd
import cv2

# a.convert_video_to_frames('DSCN9955_backgroundcutwithshadow.avi', 'DSCN9955_backgroundcutwithshadow_Frames')

# images = sd.read_files_as_images('DSCN9955_backgroundcutwithshadow_Frames')
# cv2.imshow("asd", images[25])
# cv2.waitKey(0)
#
#
# video = 'DSCN9955_backgroundcutwithshadow.avi'
# frames_without_background = 'DSCN9955_backgroundcutwithshadow_Frames'
# project/processing/DSCN9955.MOV
movie = 'processing/DSCN9955.MOV'
frames = 'processing/frames'
frameswithoutbacground = 'processing/frameswithoutBackground'
frameswithcontours = 'processing/framesWithContours'
# sd.convert_video_to_frames_withAndWithoutBackground(movie, frames, frameswithoutbacground)
contours = sd.find_contours_for_frames(frameswithoutbacground)
sd.save_frames_with_contours(contours, 'D:\\mgr projekt\\mgr\\project\\processing\\frames',
                             'D:\\mgr projekt\\mgr\\project\\processing\\' + 'framesWithContours')
# D:\mgr
# projekt\mgr\project\processing \
# convert_frames_to_video('testframesfunc', outpath)
