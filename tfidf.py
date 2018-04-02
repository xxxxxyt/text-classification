#coding=utf-8

import os
import sys
import pickle
from numpy import *
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

def calc_tfidf_matrix(articles, max_features = 2 ** 15):
    frequencier = CountVectorizer(max_features = max_features)
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform( \
            frequencier.fit_transform(articles))
    weight = tfidf.toarray()
    # print('weight = \n', weight, '\n')
    word_list = vectorizer.get_feature_names()
    print(word_list)
    return weight

def save_mat(mat, path, begin):
    ofs = open(path, 'w')
    i = begin
    while i < len(mat):
        if i % 1000 == 0:
            print('i = ', i)
            ofs.close()
            ofs = open(path, 'a')
        line = mat[i]
        for j in range(len(line)):
            # ofs.write('%f' % mat[i][j] + ' ')
            s = str(mat[i][j])
            if s == '0.0':
                s = '0'
            ofs.write(s + ' ')
        ofs.write('\n')
        i = i + 1

if __name__ == "__main__":
    """ setting path """
    path = '../dataset/train'
    print('input YES to comfirm path: '+ path)
    while True:
        s = input()
        if s == 'YES':
            break
    ifs = open(path + '_title.txt', 'r')
    articles_title = ifs.read().split('\n')
    ifs = open(path + '_content.txt', 'r')
    articles_content = ifs.read().split('\n')
    print('opening file has been done!\n')
    
    """ word freq """
    freq_mat_title = calc_tfidf_matrix(articles_title)
    freq_mat_content = calc_tfidf_matrix(articles_content)
    freq_mat = np.hstack((freq_mat_title, freq_mat_content))
    print('calculating freq mat has been done!')
    save_mat(freq_mat, path + '_freq_mat.txt', begin = 0)
    # ofs = open(path + '_freq_mat.pkl', 'wb')
    # pickle.dump(freq_mat, ofs)
    print('saving freq mat has been done!')