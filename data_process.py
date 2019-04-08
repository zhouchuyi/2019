'''  
This module is used for changing comments.csv to comments.txt

'''
import csv
import numpy as np
from nltk.corpus import stopwords
from nltk  import word_tokenize
import os
''' 
read data to list
'''
def generete_dir(name):
    curpath='/Users/zhouchouyi/topic_model'
    # print(curpath)
    targetpath=curpath+os.path.sep+name
    # print(targetpath)
    if not os.path.exists(targetpath):
        os.makedirs(targetpath)
    else:
        print("dir generate error")
    return targetpath
def process(filename,path):
    with open(filename) as f:
        reader=csv.reader(f)
        mess=list(reader)
    english_stopwords=stopwords.words('english')#stop words
    english_punctuations = [',', '.', ':', ';','(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','-','"',"'",'``',"''",'?','/','//','>','<','}','{','||','...','‘','’','=','==',"'s","'m","n't"]
    file=open(path+os.path.sep+"comments.txt",'w')
    for item in mess:
        comment=[]
        words=word_tokenize(item[6].lower())
        for word in words:
            if (word not in english_stopwords) and (word not in english_punctuations):
                comment.append(word)
        if comment!=[] :
            file.write(' '.join(comment)+'\n')
    file.close()
if __name__ == '__main__':
    # filename='comments.csv'
    # with open(filename) as f:
    #     reader=csv.reader(f)
    #     mess=list(reader)
    # comments=[]
    # english_stopwords=stopwords.words('english')#stop words
    # english_punctuations = [',', '.', ':', ';','(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','-','"',"'",'``',"''",'?','/','//','>','<','}','{','||','...','‘','’','=','==',]
    # file=open('comments2.txt','w')
    # for item in mess:
    #     comment=[]
    #     words=word_tokenize(item[6].lower())
    #     for word in words:
    #         if (word not in english_stopwords) and (word not in english_punctuations):
    #             comment.append(word)
    #             # print(word)
    #     if comment!=[] :
    #         file.write(' '.join(comment)+'\n')
    # file.close()
    path=generete_dir("data")
    process("comments.csv",path)
        