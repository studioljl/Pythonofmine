import os,requests,re
from bs4 import BeautifulSoup

import bs4

header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}

def getMax(html):
    span=re.findall(r'\<span\>\d\d\<\/span\>',html)
    r = re.compile(r'\d\d')
    x=r.findall(span[0])
    return int(x[0])

def getHTMLPages(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("")

def DealHTML(html):
    try:
        soup = BeautifulSoup(html,'html.parser')
        deal = []
        for i in soup.find_all('img'):
            deal += {i.get('src')}
        return deal[0]
    except:
        print('')

def download(folder,url):
    if not os.path.exists(folder):
        os.makedirs(folder)
    req = requests.get(url,headers=header)
    if req.status_code == requests.codes.ok:
        name = url.split('/')[-1]
        f = open("./"+'%s'%folder+'/'+'%s'%name,'wb')
        f.write(req.content)
        f.close()
        return True
    else:
        return False

def getAllPages():
    url='http://www.mzitu.com'
    r = requests.get(url,timeout=30)
    soup = r.text
    soup = BeautifulSoup(soup,'html.parser')
    lis=[]
    for link in soup.find_all('a'):
        deal = link.get('href')
        panduan = deal.split('/')[-1]
        try:
            pandaun=int(panduan)
            lis += {panduan}
        except:
            continue
    return lis

if __name__ == '__main__':
    lis = []
    lis = getAllPages()
    for num in lis:
        tru = [] 
        maxn=getMax(getHTMLPages('http://www.mzitu.com/'+num))
        for i in range(1,maxn):
            url = 'http://www.mzitu.com/'+'%s'%num+'/'+'%s'%i
            deal = getHTMLPages(url)
            q = DealHTML(deal)
            tru += {q}
            print(q)
        for url in tru:
            download(num,url) 