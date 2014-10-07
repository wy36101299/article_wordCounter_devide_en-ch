# -*- coding: utf-8 -*-
import re
import sys
import json
import jieba

class WordCounter(object):
	"""docstring for wordCounter"""
	def __init__(self):
		reload(sys)
		sys.setdefaultencoding('utf-8')
		self.l =[]
		self.data_en = ""
		self.data_ch = ""
		self.datapath = '你的文章.txt'

	def filter(self,article):
		re.sub("《|》|，|。|？|：|！|……|——|,|-|!|\.|<|>|\?|:|\r|\n","", article);
		re_words=re.compile(r"[\x80-\xff]+") 
		a =  re_words.findall(article)
		ch = ''.join(a)
		self.data_ch = jieba.cut_for_search(ch)

		en =  re_words.sub('',article)
		self.data_en = en.split(' ')

	def freqdict(self,data):
	    artdic={}
	    for a in data:
	        artdic[a]=artdic.get(a,0)+1
	    return artdic

	def storage(self,en_artdic,ch_artdic):
		a = en_artdic.copy()
		a.update(ch_artdic)
		with open('data.json', 'w') as f:
			f.write( json.dumps(a, encoding="UTF-8",indent = 4,sort_keys = True, ensure_ascii=False) )

	def run(self):
		with open(self.datapath, 'r') as f:
		    article = f.read()
		self.filter(article)
		self.storage( self.freqdict(self.data_en) , self.freqdict(self.data_ch) )

#主函數
def main() :

    wordCounter = WordCounter()
    wordCounter.run()

if __name__ == '__main__' :
    main()


