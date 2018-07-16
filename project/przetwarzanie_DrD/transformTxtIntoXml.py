# import project.boxPos as bp


def read_lines(txtfile):
    with open(txtfile) as fp:
        lines = fp.read().split("\n")
    return list(filter(None, lines))


print(read_lines('ramki/DSCN9958.MOV_ramki.txt'))


def convert_line_to_rect_with_bee(line):
    (frame, centerx, centery, radius, is_bee) = line.split(" ")[:5]
    return frame, centerx, centery, radius, is_bee


print(convert_line_to_rect_with_bee('0 1042 398 61 1 0 0 0 0 -1 5.761526 -1.000000'))


def convert_lines_to_tuples(lines):
    tuples_list = []
    for line in lines:
        tuples_list.append(convert_line_to_rect_with_bee(line))
    return tuples_list


print(convert_lines_to_tuples(read_lines('ramki/DSCN9958.MOV_ramki.txt')))


def filter_only_bees_detected(listOfTuples):
    return list(filter(lambda tup: tup[4] == '1', listOfTuples))


print(filter_only_bees_detected(convert_lines_to_tuples(read_lines('ramki/DSCN9958.MOV_ramki.txt'))))


def create_rect_from_txt_source(tuple_xyr):
    x, y, r = tuple_xyr
    return (x - r).__str__(), (y - r).__str__(), (x + r).__str__(), (y + r).__str__()


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
