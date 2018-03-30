#coding=utf-8

import jieba
import os
import numpy as np
import tensorflow as tf
import json
from bs4 import BeautifulSoup

def deal_with_content(content):
    """ tag free """
    soup = BeautifulSoup(content)
    content = soup.get_text()
    """ segment """
    seg_list = jieba.cut(content) #, cut_all = True)
    content = ",".join(seg_list)
    content = content.split(',')
    """ stop word free """
    stop_list = {}.fromkeys([line.strip() for line in open("dict/stop-list.txt")])
    content = [word for word in content if word not in stop_list
                                       and word != '\u3000'
                                       and word != '\xa0']
    return content

if __name__ == "__main__":
    ifs = open("../dataset/train.json", 'r')
    while (True):
        article_json = ifs.readline()
        article = json.loads(article_json)
        id = article['id']
        title = deal_with_content(article['title'])
        content = deal_with_content(article['content'])
        print(content)
        print("\nPress any key to conitnue...\n")
        input()