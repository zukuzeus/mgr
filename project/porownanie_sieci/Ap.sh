#!/bin/bash

GROUNDTRUTH="C:\mgr\mgr\project\porownanie_sieci\drDębski\groundtruth"

DETECTION="C:\mgr\mgr\project\porownanie_sieci\drDębski\detections"

FORMAT=xyrb

PASCALVOCPATH="C:\mgr\tensor\Object-Detection-Metrics"


python $PASCALVOCPATH/pascalvoc.py -t 0.75 \
-gtformat $FORMAT -detformat $FORMAT \
-gt $GROUNDTRUTH -det $DETECTION



