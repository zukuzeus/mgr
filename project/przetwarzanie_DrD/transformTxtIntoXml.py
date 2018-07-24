from tqdm import tqdm

import project.boxPos as bp
import itertools
import project.simpleDetecting as det


def read_lines(txtfile):
    with open(txtfile) as fp:
        lines = fp.read().split("\n")
    return list(filter(None, lines))


# 'ramki/DSCN9958.MOV_ramki.txt'
# project/przetwarzanie_DrD/ramki/DSCN9949.MOV_ramki.txt
filename = 'DSCN9954'
txtFileWithFrame = 'D:\\mgr projekt\\mgr\project\\przetwarzanie_DrD\\ramki\\' + filename + '.MOV_ramki.txt'
print(read_lines(txtFileWithFrame))


def convert_line_to_rect_with_bee(line):
    (frame, centerx, centery, radius, is_bee) = line.split(" ")[:5]
    return frame, centerx, centery, radius, is_bee


print(convert_line_to_rect_with_bee('0 1042 398 61 1 0 0 0 0 -1 5.761526 -1.000000'))


def convert_lines_to_tuples(lines):
    tuples_list = []
    for line in lines:
        tuples_list.append(convert_line_to_rect_with_bee(line))
    return tuples_list


framesLinesWithData = convert_lines_to_tuples(read_lines(txtFileWithFrame))
print("lines",framesLinesWithData.__len__(),framesLinesWithData)


def filter_only_bees_detected(listOfTuples):
    return list(filter(lambda tup: tup[4] == '1', listOfTuples))


filteredBees = filter_only_bees_detected(framesLinesWithData)
print("filtered", filteredBees.__len__(),filteredBees)

sortedInput = sorted(filteredBees, key=lambda item: int(item[0]))
print("sorted", sortedInput.__len__(), sortedInput)

groups = []
uniquekeys = []
for k, g in itertools.groupby(sortedInput, key=lambda tup: int(tup[0])):
    groups.append(list(g))  # Store group iterator as a list
    uniquekeys.append(k)

print(filter_only_bees_detected(framesLinesWithData))

print(sortedInput)
print("groups",groups.__len__(),groups)
for gr in groups:
    print(gr)


def create_rect_from_txt_source(tuple_xyr):
    x, y, r = tuple_xyr
    x = int(x)
    y = int(y)
    r = int(r)
    return (x - r).__str__(), (y - r).__str__(), (x + r).__str__(), (y + r).__str__()


# bp.crea
filesToSave = []

pathToSaveXmls = "D:\\mgr projekt\\mgr\\project\\" + filename + "_xmls\\"
for frames in tqdm(groups):
    # print(frames[0][0])
    framePath = "/frames/" + filename + "_" + "frame"
    frameNum = frames[0][0]
    xmlFile = bp.createXmlForFrame(framePath + frameNum, (1920, 1080, 3))
    objectNodes = []
    for rect in frames:
        # create file for frame
        objectNode = bp.createXmlNodeForObject((rect[1], rect[2], rect[3]), fun=create_rect_from_txt_source)
        objectNodes.append(objectNode)
    finalfile = bp.appendXmlObjectsToXml(xmlFile, objectNodes)
    filesToSave.append(finalfile)
    bp.saveXml(finalfile, frameNum, pathToSaveXmls)
# print(filesToSave)

# bp.saveXmls(filesToSave, pathToSaveXmls)
# print(filesToSave)
# det.convert_video_to_frames("","")

# bp.createXmlNodeForObject()

# bp.createXmlsForFrames()

#    <object>
# 		<name>bee</name>
# 		<pose>Unspecified</pose>
# 		<truncated>0</truncated>
# 		<difficult>0</difficult>
# 		<bndbox>
# 			<xmin>1249</xmin>
# 			<ymin>857</ymin>
# 			<xmax>1455</xmax>
# 			<ymax>986</ymax>
# 		</bndbox>
# 	</object>
