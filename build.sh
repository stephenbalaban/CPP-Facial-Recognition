#!/bin/bash
echo 'g++ `pkg-config --cflags opencv` `pkg-config --libs opencv` -o OnlineFaceRec OnlineFaceRec.cpp'
g++ `pkg-config --cflags opencv` `pkg-config --libs opencv` -o OnlineFaceRec OnlineFaceRec.cpp
echo 'Done. Run ./OnlineFaceRec'
