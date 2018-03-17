import project.simpleDetecting as sd
import cv2
from xml.dom import minidom
import xml.etree.ElementTree as ET
import os

framesContours = 'D:\\mgr projekt\\mgr\\project\\processing\\' + 'frameswithoutBackground'
frames = 'D:\\mgr projekt\\mgr\\project\\processing\\' + 'frames'
contours = sd.find_contours_for_frames(framesContours)
xmlfolderpath = 'D:\\mgr projekt\\mgr\\project\\processing\\' + 'xml'


# rectanglesForImages = []

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


def appendObjectsToXml(xml, rectangles):
    tree = ET.ElementTree(xml)
    root = tree.getroot()
    for r in rectangles:
        root.append(createXmlNodeForObject(r))

    finalFile = ET.tostring(root, encoding='unicode')
    return finalFile


def createXmlForFrame(pathToFile, imgSize):
    annotation = ET.Element('annotation')
    folder = ET.SubElement(annotation, 'folder')
    filename = ET.SubElement(annotation, 'filename')
    path = ET.SubElement(annotation, 'path')
    source = ET.SubElement(annotation, 'source')
    database = ET.SubElement(source, 'database')
    size = ET.SubElement(annotation, 'size')
    width = ET.SubElement(size, 'width')
    height = ET.SubElement(size, 'height')
    depth = ET.SubElement(size, 'depth')
    segmented = ET.SubElement(annotation, 'segmented')
    folder.text = os.path.basename(os.path.dirname(pathToFile))
    filename.text = os.path.basename(pathToFile)
    path.text = pathToFile.replace("\\", "/")
    database.text = 'Unknown'
    w, h, d = imgSize
    width.text = w.__str__()
    height.text = h.__str__()
    depth.text = d.__str__()

    segmented.text = '0'

    xmlfile = annotation
    return xmlfile


def createXmlNodeForObject(rect):
    object = ET.Element('object')
    name = ET.SubElement(object, 'name')
    name.text = 'bee'
    pose = ET.SubElement(object, 'pose')
    pose.text = 'Unspecified'
    truncated = ET.SubElement(object, 'truncated')
    truncated.text = '0'
    difficult = ET.SubElement(object, 'difficult')
    difficult.text = '0'
    bndbox = ET.SubElement(object, 'bndbox')
    xmin = ET.SubElement(bndbox, 'xmin')
    ymin = ET.SubElement(bndbox, 'ymin')
    xmax = ET.SubElement(bndbox, 'xmax')
    ymax = ET.SubElement(bndbox, 'ymax')

    x, y, w, h = rect

    xmin.text, ymin.text, xmax.text, ymax.text = (x.__str__(), y.__str__(), (x + w).__str__(), (y + h).__str__())

    return object


rectanglesForImages = getRectanglesFromContours(contours)


fullpaths = sd.get_sorted_filelist_full_paths(frames)
def createXmlsForFrames(filePathlist):
    xmls = []
    counter = 0
    for filepath in fullpaths:
        xmlstringfile = appendObjectsToXml(createXmlForFrame(filepath, (1920, 1080, 3)), rectanglesForImages[counter])
        xmls.append(xmlstringfile)
        counter += 1
    return xmls


# XMLs
xmls = createXmlsForFrames(fullpaths)


def saveXmls(xmlList, path):
    counter = 0
    for xml in xmlList:
        f = open(os.path.join(path, "frame{}.xml".format(counter)), 'w')
        f.write(xml)
        f.close()
        counter += 1


saveXmls(xmls, xmlfolderpath)
# os.path.splitext(os.path.basename("hemanth.txt"))[0] = nazwa pliku ze ścieżki
f = 1
