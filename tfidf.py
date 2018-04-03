#coding=utf-8

import os
import sys
import pickle
import numpy as np
import scipy
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

def calc_tfidf_matrix(articles, max_features = 2 ** 12):
    vectorizer = CountVectorizer(max_features = max_features)
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform( \
            vectorizer.fit_transform(articles))
    # weight = tfidf.toarray()
    # print('weight = \n', weight, '\n')
    word_list = vectorizer.get_feature_names()
    # print(word_list)
    return [tfidf, word_list]

if __name__ == "__main__":

    print('input YES to comfirm: ')
    while True:
        s = input()
        if s == 'YES':
            break

    """ read in data """
    path = '../dataset/'
    ifs = open(path + 'seg_title.pkl', 'rb')
    seg_title = pickle.load(ifs)
    ifs = open(path + 'seg_content.pkl', 'rb')
    seg_content = pickle.load(ifs)
    print('opening file has been done!\n')

    """ word freq """
    [freq_mat_title, feature_title] = \
        calc_tfidf_matrix(seg_title, max_features= 2 ** 10)
    print('calculating freq mat title has been done!')
    [freq_mat_content, feature_content] = \
        calc_tfidf_matrix(seg_content, max_features= 2 ** 15)
    print('calculating freq mat content has been done!')
    freq_mat = scipy.sparse.hstack((freq_mat_title, freq_mat_content))
    print('merging freq mats has been done!')
    # save_mat(freq_mat, path + 'freq_mat.txt', begin = 0)
    ofs = open(path + 'freq_mat.pkl', 'wb')
    pickle.dump(freq_mat, ofs)
    ofs = open(path + 'feature_title.pkl', 'wb')
    pickle.dump(feature_title, ofs)
    ofs = open(path + 'feature_content.pkl', 'wb')
    pickle.dump(feature_content, ofs)
    print('saving freq mat has been done!')