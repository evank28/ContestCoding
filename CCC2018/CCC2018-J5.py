#CCC2018 J5
#NOTE- SOLVED AFTER TIME EXPIRED

N=input()
book={}
pageList=[]
for i in range (0,N):
    line=input().split(" ")
    book.setdefault(i+1, {'optCount':line[0], 'options':line[1:]})
    pageList+=[i]
    
visited=[]
que=[]




for page in book:
    pageResult= book[page]
    if not (page in visited):
        if pageResult['optCount']>0:
            for childPage in pageResult['options']:
                if (childPage in pageList):
                    que=pageList.pop(childPage)
        visited+=[page]        
        
    
