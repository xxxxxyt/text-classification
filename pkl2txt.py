#coding=utf-8

import os
import sys
import pickle

if __name__ == "__main__":
    ifs = open('../dataset/seg_content.pkl', 'rb')
    seg = pickle.load(ifs)
    ofs = open('../dataset/seg.txt', 'w')
    ofs.write('\n'.join(seg))