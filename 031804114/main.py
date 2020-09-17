#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# author: xm time:2020/9/17
# ！/usr/bin/env python
# _*_ coding:utf-8 _*_
# author: xm time:2020/9/16
from __future__ import division
from math import sqrt
import jieba.analyse
from functools import reduce
import sys


# jieba包进行分词
# 利用余弦定理计算


class Similarity():
    def __init__(self, target1, target2, topK=30):
        self.target1 = target1
        self.target2 = target2
        self.topK = topK

    # jieba分词分析操作,可参考网上使用
    def vector(self):
        self.vdict1 = {}
        self.vdict2 = {}
        top_keywords1 = jieba.analyse.extract_tags(self.target1, topK=self.topK, withWeight=True)
        top_keywords2 = jieba.analyse.extract_tags(self.target2, topK=self.topK, withWeight=True)
        for k, v in top_keywords1:
            self.vdict1[k] = v
        for k, v in top_keywords2:
            self.vdict2[k] = v

    def mix(self):
        for key in self.vdict1:
            self.vdict2[key] = self.vdict2.get(key, 0)
        for key in self.vdict2:
            self.vdict1[key] = self.vdict1.get(key, 0)

        # 计算相对词频，文章的长度可能不一致，所以关键词词频率可以使用相对词频率
        def mapminmax(vdict):
            _min = min(vdict.values())
            _max = max(vdict.values())
            _mid = _max - _min
            # print _min, _max, _mid
            for key in vdict:
                vdict[key] = (vdict[key] - _min) / _mid
            return vdict

        self.vdict1 = mapminmax(self.vdict1)
        self.vdict2 = mapminmax(self.vdict2)

    def similar(self):
        self.vector()
        self.mix()
        sum = 0
        for key in self.vdict1:
            sum += self.vdict1[key] * self.vdict2[key]
        A = sqrt(reduce(lambda x, y: x + y, map(lambda x: x * x, self.vdict1.values())))
        B = sqrt(reduce(lambda x, y: x + y, map(lambda x: x * x, self.vdict2.values())))
        return sum / (A * B)


# 打开并读取文件
if __name__ == '__main__':
    # file1=open(r"D:\machine learn\softproject\sim_0.8\orig.txt","r",encoding='UTF-8')
    # 从命令行读取绝对路径
    x1 = sys.argv[1]
    x2 = sys.argv[2]
    x3 = sys.argv[3]

    file1 = open(x1, 'r', encoding='utf-8')
    file2 = open(x2, 'r', encoding='utf-8')

    txt1 = file1.read()
    txt2 = file2.read()

    file1.close()
    file2.close()
    # 采用分词，复杂度较高，可以采用TF-IDF的方式找出文章若干个关键词，再进行比较
    topK = 800  # 关键词数量 该数值会影响相似度
    s = Similarity(txt1, txt2, topK)
    result = s.similar()
    result = round(result, 2)
    with open(x3, "w") as f:
        f.write(str(result))
    f.close()
 
