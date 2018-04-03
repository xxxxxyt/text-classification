#coding=utf-8

import os
import sys
import pickle

if __name__ == "__main__":
    ifs = open('../dataset/train.csv', 'r')
    y = ifs.read().split('\n')
    y.pop(0)
    y.pop(-1)
    y = [int(line.split(',')[1]) for line in y]
    ofs = open('../dataset/label.pkl', 'wb')
    pickle.dump(y, ofs)