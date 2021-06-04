
import newspaper
import pandas as pd
from docx import Document
import os
from newspaper import Config
import sys

#C:\Users\saha\AppData\Local\Temp\.newspaper_scraper\memoized

    
class GetNews(object):
    def __init__(self):
        urls = pd.read_excel('url.xls')
        self.urlList = urls['url'] 
        keywords = pd.read_excel('keyWord.xls')
        self.keywordList = []
        for j in range(0, len(keywords)):
            tmp = keywords.iloc[j]['keywords']     
            arr = tmp.split(';')
            self.keywordList.extend(arr[:-1])
        
        if not os.path.exists('result'):
            os.mkdir('result')
            
        
        
    def readNews(self):
        news_title = []
        news_text = []
        news_urls = []
        news_keys = []
        news_date = []
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
        config = Config()
        config.browser_user_agent = user_agent
        config.fetch_images = False
        config.request_timeout = 20
        config.number_threads = 1
        config.keep_article_html = True
        i = 0
        for url in self.urlList:   
            i = i + 1
            print(str(i) + "  " + url)
            newsSource = newspaper.build(url,config=config)             
            for paper in newsSource.articles:
                try :
                    paper.download()
                    paper.parse()
                    #print('parse')
                    res = self.keyWordMatch(paper.text,paper.title)
                    if len(res)>0:
                        print('hint: ' + paper.title)
                        news_title.append(paper.title)     # 将新闻题目以列表形式逐一储存
                        news_text.append(paper.text)       # 将新闻正文以列表形式逐一储存
                        news_urls.append(paper.url)
                        news_keys.append(res)
                        pDate=''
                        if paper.publish_date is not None:
                            pDate = paper.publish_date.strftime('%Y-%m-%d')
                            print(pDate)
                        news_date.append(pDate)                            
                        self.saveFile(pDate,paper.url,res,paper.title,paper.text)
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                    continue
                
        data = pd.DataFrame({'title':news_title,'key':news_keys,'date':news_date,'url':news_urls})
        data.to_excel('result/result.xls',sheet_name='result')
        print(news_date)
        print('finished!')
                
    def keyWordMatch(self, text,title):
        for keyword in self.keywordList:
            if keyword in title:
                return keyword
            if keyword in text:
                return keyword
        
        return ''
    
    def saveFile(self,pb_date,url,keyWord,title,body):
        document = Document()
        document.add_heading(title, 0)
        p=document.add_paragraph('')
        p.add_run('url: ' + url + '\n').bold = True
        p.add_run('publish_date: ' + pb_date + '\n').bold = True
        p.add_run('match key_word: ' + keyWord + '\n').bold = True
        p.add_run(body)
        document.add_page_break()
        document.save('result/'+ title +'.docx')
        
        
            
if __name__ == '__main__':
    ins = GetNews()
    ins.readNews()
