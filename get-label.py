#coding=utf-8

import os
import sys
import pickle

if __name__ == "__main__":
    ifs = open('../dataset/predict/90628_/submit.csv', 'r')
    y = ifs.read().split('\n')
    y.pop(0)
    y.pop(-1)
    y = [float(line.split(',')[1]) for line in y]
    y.append(0.00)
    ofs = open('../dataset/y_test.pkl', 'wb')
    pickle.dump(y, ofs)