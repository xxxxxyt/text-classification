#coding=utf-8

import os
import sys
import json
import jieba
from bs4 import BeautifulSoup

def deal_with_content(content, stop_list):
    """ tag free """
    soup = BeautifulSoup(content, 'html5lib')
    content = soup.get_text()
    """ segment """
    seg_list = jieba.cut(content) #, cut_all = True)
    content = ','.join(seg_list)
    content = content.split(',')
    """ stop word free """
    content = [word for word in content if word not in stop_list
                                       and word != '\n'
                                       and word != ' '
                                       and word != '　']
    """ number """
    for i in range(len(content)):
        word = content[i]
        if '%' in word:
            content[i] = '%'
        if '.' in word:
            content[i] = '.'
    return content

if __name__ == "__main__":

    stop_list = {}.fromkeys([line.strip() for line in open('dict/stop-list.txt')])

    """ setting path """
    path = '../dataset/train'
    print('input YES to comfirm path: '+ path)
    while True:
        s = input()
        if s == 'YES':
            break
    ifs = open(path + '.json', 'r')
    print('opening file has been done!\n')

    """ read in articles """
    articles_raw = ifs.read().split('\n')
    articles_title = []
    articles_content = []
    for i in range(len(articles_raw) - 1):
    # for i in range(2000):
        if i % 1000 == 0:
            print('i = ', i)
        article = json.loads(articles_raw[i])
        id = article['id']
        title = ' '.join(deal_with_content(article['title'], stop_list))
        content = ' '.join(deal_with_content(article['content'], stop_list))
        articles_title.append(title)
        articles_content.append(content)
        # print("\nPress any key to conitnue...\n")
        # input()
    print('reading in articles has been done!\n')
    
    """ write segment """
    ofs = open(path + '_title.txt', 'w')
    ofs.write('\n'.join(articles_title))
    ofs = open(path + '_content.txt', 'w')
    ofs.write('\n'.join(articles_content))
    print('writing segment has been done!')