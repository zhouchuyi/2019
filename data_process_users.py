''' 
this module is used to generate 10 users data 
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
    mess=mess[1:]
    english_stopwords=stopwords.words('english')#stop words
    english_punctuations = [',', '.', ':', ';','(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','-','"',"'",'``',"''",'?','/','//','>','<','}','{','||','...','‘','’','=','==',"'s","'m","n't"]
    id=1
    line=0
    file=open(path+os.path.sep+"user1.txt",'w')
    # file=open(path+os.path.sep+"user{}.txt".format(i),'w')
    # for i in range(1,11):
    #     file=open(path+os.path.sep+"user{}".format(i),'w')
    #     for item in mess:
    #         if user_id==item[2]:
    #             comment=[]
    #             words=word_tokenize(item[6].lower())
    #             for word in words:
    #                 if (word not in english_stopwords) and (word not in english_punctuations):
    #                     comment.append(word)
    #             if comment!=[] :
    #                 file.write(' '.join(comment)+'\n')
    #
    #             file.close()
    cnt=0
    for item in mess:
        comment=[]
        words=word_tokenize(item[6].lower())
        for word in words:
            if (word not in english_stopwords) and (word not in english_punctuations):
                comment.append(word)
            # print(word)
        if comment!=[] :
            if id==item[2]:
                file.write(' '.join(comment)+' ')
            else:
                file.close()
                id=item[2]
                line+=1
                if(line>11):
                    break
                file=open('user'+str(id)+'.txt','w')
                file.write(' '.join(comment)+'\n')

if __name__ == '__main__':
    path=generete_dir("users")
    process("/Users/zhouchouyi/topic_model/comments.csv",path)
    
