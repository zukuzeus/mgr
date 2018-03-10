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
sd.convert_video_to_frames_withAndWithoutBackground('processing/DSCN9955.MOV')

# convert_frames_to_video('testframesfunc', outpath)
