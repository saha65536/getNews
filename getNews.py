
import newspaper
import pandas as pd

    
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
            
        
        
    def readNews(self):
        news_title = []
        news_text = []
        news_urls = []
        news_keys = []
        for url in self.urlList:            
            print(url)
            newsSource = newspaper.build(url, language='zh')             
            for paper in newsSource.articles:
                try :
                    paper.download()
                    paper.parse()
                    res = self.keyWordMatch(paper.text,paper.title)
                    if len(res)>0:
                        news_title.append(paper.title)     # 将新闻题目以列表形式逐一储存
                        news_text.append(paper.text)       # 将新闻正文以列表形式逐一储存
                        news_urls.append(paper.url)
                        news_keys.append(res)
                except:
                    news_urls.append(paper.url)
                    news_title.append('NULL')          # 如果无法访问，以NULL替代
                    news_text.append('NULL')   
                    news_keys.append('NULL')
                    continue
                
        date = pd.DataFrame({'title':news_title,'key':news_keys,'url':news_urls,'text':news_text})
        date.to_csv('result.csv',index=False,sep=',')
                
    def keyWordMatch(self, text,title):
        for keyword in self.keywordList:
            if keyword in title:
                return keyword
            if keyword in text:
                return keyword
        
        return ''
        
            
if __name__ == '__main__':
    ins = GetNews()
    ins.readNews()