
import pandas as pd
import numpy as np
import jieba
import re

def split_words(filein,fileout):
    name = ['website' ,'jobname' ,'company' ,'salary',
            'adress' ,'Releasedate' ,'partOrfull',
            'experience' ,'education' ,'need',
            'workname' ,'jobinfo']
    df = pd.read_csv('./'+filein ,delimiter='\t' ,encoding='utf-8', header=None, names=name)

    jobinfos = df[:]['jobinfo']  # 工作信息

    words = []
    JobSkillPartten = re.compile('任职要求[：|:](.*?)工作地址')
    for jobinfo in jobinfos:
        JobSkill = re.findall(JobSkillPartten, str(jobinfo).replace("  ", ""))
        if len(JobSkill) > 0:
            result = jieba.cut(JobSkill[0], cut_all=False)
            for word in result:
                if len(word) > 1:
                    words.append(word)

    KeyWords = pd.DataFrame({'word': words})

    grouped = KeyWords.groupby('word')

    wordsresult = grouped['word'].agg({'计数': np.size}).reset_index().sort(columns=['计数'], ascending=False)
    wordsresult.to_csv(fileout)

if __name__ == '__main__':

    import zhilian

    print("开始采集------------")
    city = '上海'
    keyWord = 'php'
    #城市，关键词，最近几天，抓取几页数据（默认全部）
    items = zhilian.getJobSite(city, keyWord, 7, 10)
    filename = city + keyWord + '.txt'

    zhilian.getJobInfo(items,filename)
    print("采集结束------------")
    # print("开始分词------------")
    # filein = filename
    # fileout = 'keywordsof'+filein
    # split_words(filein,fileout)
    # print("分词结果见----"+fileout+"----")
