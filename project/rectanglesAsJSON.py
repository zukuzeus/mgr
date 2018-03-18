import json
import project.simpleDetecting as sd
import cv2

jsonobj = [[[1,2,3,4],[5,6,7,8]],[[1,2,3,4]],[[1,2,5,7]],[[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]]]


def rectJsonToRectTuplesList(framesRects):
    listsOfTuples = []
    for lists in framesRects:
        listsOfTuples.append([tuple(l) for l in lists])
    return listsOfTuples


rectJsonToRectTuplesList(jsonobj)


framesContours = 'D:\\mgr projekt\\mgr\\project\\processing\\' + 'frameswithoutBackground'
contours = sd.find_contours_for_frames(framesContours)
def getRectanglesFromContours(contoursForMultipleImages):
    rectanglesForImages = []
    for contoursInSingleImage in contoursForMultipleImages:
        rectangles = contorusToRectangles(contoursInSingleImage)
        rectanglesForImages.append(rectangles)
    return rectanglesForImages


def contorusToRectangles(contours):
    rectangles = []
    for c in contours:
        d = cv2.boundingRect(c)
        rectangles.append(d)
    return rectangles

with open('D:\\mgr projekt\\mgr\\project\\processing\\'+'rect.json', 'w') as outfile:
    json.dump(getRectanglesFromContours(contours),outfile,indent=4)

