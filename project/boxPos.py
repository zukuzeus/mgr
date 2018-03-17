import project.simpleDetecting as sd
import cv2
from xml.dom import minidom
import xml.etree.ElementTree as ET
import os

frames = 'D:\\mgr projekt\\mgr\\project\\processing\\' + 'frameswithoutBackground'
contours = sd.find_contours_for_frames(frames)

rectanglesForImages = []
for conts in contours:
    tuples = []
    for c in conts:
        d = (x, y, w, h) = cv2.boundingRect(c)
        tuples.append(d)
    rectanglesForImages.append(tuples)


def appendObjectsToXml(xml, rectangles):
    tree = ET.ElementTree(ET.fromstring(xml))
    root = tree.getroot()
    for r in rectangles:
        root.append(createXmlNodeForObject(r))

    finalFile = ET.tostring(tree)
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
    path.text = pathToFile.replace("\\","/")
    database.text = 'Unknown'
    w, h, d = imgSize
    width.text = w.__str__()
    height.text = h.__str__()
    depth.text = d.__str__()

    segmented.text = '0'

    xmlfile = ET.tostring(annotation)

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


# XMLs
fullpaths = sd.get_sorted_filelist_full_paths(frames)
counter = 0
for filepath in fullpaths:
    xmlstring = createXmlForFrame(filepath, (1920, 1080, 3))
    # rectanglesForImages[counter]
    xmlstringfile = appendObjectsToXml(xmlstring, rectanglesForImages[counter])
    counter += 1

    # createXmlForFrame()
# os.path.splitext(os.path.basename("hemanth.txt"))[0] = nazwa pliku ze ścieżki
