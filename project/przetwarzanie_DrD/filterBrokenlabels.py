import os
import xml.etree.ElementTree as ET
from tqdm import tqdm

path = 'D:\\klatki_z_filmow\\mieszanka'


def evaluate_if_box_is_inside_image(object):
    isBoxValid = True
    bndbox = object.find('bndbox')
    xmin = int(bndbox.find('xmin').text)
    ymin = int(bndbox.find('ymin').text)
    xmax = int(bndbox.find('xmax').text)
    ymax = int(bndbox.find('ymax').text)
    szerokosc = 1920
    wysokosc = 1080
    if xmin <= 1 | xmin >= szerokosc:
        isBoxValid = False
    if ymin <= 1 | ymin >= wysokosc:
        isBoxValid = False
    if xmax <= 1 | xmax >= szerokosc:
        isBoxValid = False
    if ymax <= 1 | ymax >= wysokosc:
        isBoxValid = False
    return isBoxValid


list_of_corrupt_files = []
for filename in tqdm(os.listdir(path)):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename)
    tree = ET.parse(fullname)
    for object in tree.findall('object'):
        if not evaluate_if_box_is_inside_image(object):
            list_of_corrupt_files.append(filename)
            continue


print(list_of_corrupt_files)
for file in list_of_corrupt_files:
    print(file)
print(list_of_corrupt_files.__len__())