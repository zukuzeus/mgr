from decimal import Decimal, getcontext

getcontext().prec = 6


def get_iou_tup(bb1, bb2):
    get_iou(tuple_to_dict(bb1), tuple_to_dict(bb2))


def get_iou(bb1, bb2):
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.

    Parameters
    ----------
    bb1 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x1, y1) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner
    bb2 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x, y) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner

    Returns
    -------
    Decimal
        in [0, 1]
    """
    getcontext().prec = 6
    assert bb1['x1'] < bb1['x2']
    assert bb1['y1'] < bb1['y2']
    assert bb2['x1'] < bb2['x2']
    assert bb2['y1'] < bb2['y2']

    # determine the coordinates of the intersection rectangle
    x_left = max(bb1['x1'], bb2['x1'])
    y_top = max(bb1['y1'], bb2['y1'])
    x_right = min(bb1['x2'], bb2['x2'])
    y_bottom = min(bb1['y2'], bb2['y2'])

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    # The intersection of two axis-aligned bounding boxes is always an
    # axis-aligned bounding box
    intersection_area = Decimal((x_right - x_left) * (y_bottom - y_top))

    # compute the area of both AABBs
    bb1_area = Decimal((bb1['x2'] - bb1['x1']) * (bb1['y2'] - bb1['y1']))
    bb2_area = Decimal((bb2['x2'] - bb2['x1']) * (bb2['y2'] - bb2['y1']))

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = Decimal(intersection_area / (bb1_area + bb2_area - intersection_area))
    assert iou >= 0.0
    assert iou <= 1.0
    return iou


# print(get_iou({'x1': float(0.14201183431952663), "x2": float(0.23076923076923078),
#                "y1": float(0.7511111111111111), "y2": float(0.9688888888888889)},
#               {'x1': float(0.15993668), "x2": float(0.21673931), "y1": float(0.77961), "y2": float(0.94080526)}))
def tuple_to_dict(tup):
    """
    transform tuple of (x1,y1,x2,y2) into dict {'x1', 'x2', 'y1', 'y2'}
    """
    return {'x1': tup[0], "x2": tup[2],
            "y1": tup[1], "y2": tup[3]}


print(get_iou({'x1': Decimal(0.1), "x2": Decimal(0.2),
               "y1": Decimal(0.3), "y2": Decimal(0.4)},
              {'x1': Decimal(0.18), "x2": Decimal(0.2),
               "y1": Decimal(0.31), "y2": Decimal(0.4)}))

# x1,y1,x2,y2
# thruth
# bee 0.14201183431952663 0.7511111111111111 0.23076923076923078 0.9688888888888889

# detect
# bee 0.9843737 0.15993668 0.77961 0.21673931 0.94080526
