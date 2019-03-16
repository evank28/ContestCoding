#CCC2018 J5
N=input()
book={}
pageList=[]
for i in range (0,N):
    line=input().split(" ")
    book.setdefault(i+1, {'optCount':line[0], 'options':line[1:]})
    pageList+=[i]
    
def dfs(G, s):
    visited+=s
    for child in book[s]['options']:
        if not (child in visited):
            dfs(book,child)
    

