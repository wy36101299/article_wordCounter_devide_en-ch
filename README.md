article_wordCounter_devide_en-ch
================================

#大量文章-中英分離字詞-計數器  

可在大量文章中把中文和英文分離出來，別且計算每個詞彙出現的個數  
文章存放于Data folder中，並輸出Json folder 檔案格式為json  
英文分離方法為切空白  
中文分離方法為使用 jieba  

#如何使用
把要分析的文章放到Data folder即可，檔案格式需為 .txt  
分析結果輸出在Json folder中，檔案格式為文章名的 .json  

#example
Data folder 兩篇文章 test1.txt,test2.txt  
Json folder 輸出  test1.json,test2.json  
