# -*- coding: utf-8 -*-
import re
import sys
import json
import glob 
import jieba

class WordCounter(object):
	"""docstring for wordCounter"""
	def __init__(self):
		reload(sys)
		sys.setdefaultencoding('utf-8')
		self.data_en = ""
		self.data_ch = ""

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

	def storage(self,en_artdic,ch_artdic,name):
		a = en_artdic.copy()
		a.update(ch_artdic)
		with open('./Json/'+name+'.json', 'w') as f:
			f.write( json.dumps(a, encoding="UTF-8",indent = 4,sort_keys = True, ensure_ascii=False) )

	def run(self):
		path = './Data/*.txt'   
		paths=glob.glob(path)
		dic ={}
		for index, tmp in enumerate(paths):
			a = tmp.split('/')
			name = a[2].split('.')
			with open(tmp, 'r') as f:
			    article = f.read()
			self.filter(article)
			self.storage( self.freqdict(self.data_en) , self.freqdict(self.data_ch) ,name[0] )
			print('creat'+'--'+str(index)+'--'+name[0]+'.json')
			dic[index]=name[0]

		with open('./Json/index.json', 'w') as f:
			f.write( json.dumps(dic, encoding="UTF-8",indent = 4,sort_keys = True, ensure_ascii=False) )
		print('index.json creat!' )
#main
def main() :
    wordCounter = WordCounter()
    wordCounter.run()

if __name__ == '__main__' :
    main()


