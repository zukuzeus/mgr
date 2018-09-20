from argparse import ArgumentParser
import os.path
import itertools


def main():
    parser = ArgumentParser()
    parser.add_argument("-in", "--inputfile", dest="filename",
                        help="read File to process into pascalvoc format", metavar="file",
                        type=lambda x: is_valid_file(parser, x))

    args = parser.parse_args()
    lines = read_lines(args.filename)
    objectsFromFile = convert_lines_to_tuples(lines)
    grouppedFramesTuples = group_by_frames(objectsFromFile)
    save_to_files(grouppedFramesTuples)


def save_to_files(grouppedFramesTuples, savedir="output"):
    if not os.path.exists(os.path.join(os.getcwd(), savedir)):
        os.makedirs(os.path.join(os.getcwd(), savedir))

    for frame in grouppedFramesTuples:
        frameNum = frame[0][0]
        lines_ready_to_write = transformIntoTxtWritableLines(frame)
        f = open(os.path.join(os.getcwd(), savedir, "frame{}.txt".format(frameNum)), "w+")
        for line in lines_ready_to_write:
            f.write(line)
        f.close()


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle


def read_lines(file):
    lines = file.read().split("\n")
    lines_to_return = list(filter(None, lines))
    lines_to_return.pop(0)
    return lines_to_return


def convert_line_to_tuple_for_write(line):
    """
    :param line: format is : 0 1212 955 45 1 -1 1 1 1 -1 -1.000000 -1.000000 1.000000
    :return: tuple with frame, centerx, centery, radius, is_bee, probability
    """
    items_in_line = line.split(" ")
    (frame, centerx, centery, radius, is_bee) = items_in_line[:5]
    probability = items_in_line[-1]
    (xmin, ymin, xmax, ymax) = create_rect_from_txt_source((centerx, centery, radius), (1920, 1080))
    return frame, probability, xmin, ymin, xmax, ymax


def convert_lines_to_tuples(lines):
    tuples_list = []
    for line in lines:
        tuples_list.append(convert_line_to_tuple_for_write(line))
    return sorted(tuples_list, key=lambda item: int(item[0]))


def group_by_frames(tuples_from_frames):
    groups = []
    uniquekeys = []
    for k, g in itertools.groupby(tuples_from_frames, key=lambda tup: int(tup[0])):
        groups.append(list(g))  # Store group iterator as a list
        uniquekeys.append(k)
    return groups


def create_rect_from_txt_source(tuple_xyr, image_size):
    def normalize(value, dividor):
        return value / dividor

    width, heigth = image_size
    width = int(width)
    heigth = int(heigth)
    x, y, r = tuple_xyr
    x = int(x)
    y = int(y)
    r = int(r)
    xmin = normalize((x - r), width)
    xmax = normalize((x + r), width)
    ymin = normalize((y - r), heigth)
    ymax = normalize((y + r), heigth)
    return xmin.__str__(), ymin.__str__(), xmax.__str__(), ymax.__str__()


def transformIntoTxtWritableLines(tuplesList):
    def tranformTupleIntoWritableFormat(tuple):
        return "bee", tuple[1], tuple[2], tuple[3], tuple[4], tuple[5]

    listOfWritableObjects = []
    for e in tuplesList:
        listOfWritableObjects.append(' '.join(str(x) for x in tranformTupleIntoWritableFormat(e)) + "\n")
    return listOfWritableObjects


if __name__ == "__main__":
    main()
