#!/bin/bash

GROUNDTRUTH="C:\mgr\mgr\project\porownanie_sieci\rcnn\groundtruth"

DETECTION="C:\mgr\mgr\project\porownanie_sieci\ssd\detections"

FORMAT=xyrb

PASCALVOCPATH="C:\mgr\tensor\Object-Detection-Metrics"


python $PASCALVOCPATH/pascalvoc.py -t 0.5 \
-gtformat $FORMAT -detformat $FORMAT \
-gt $GROUNDTRUTH -det $DETECTION



