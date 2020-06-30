import requests
from tkinter import *
root=Tk()
results=[]
def LatestNews():
    
  url=('http://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=7b2382cdd48b4f6a9964745f415abe6f')
  res=requests.get(url).json()
  global root
  top_news=res["articles"]
  global results
  
  for i in top_news:
      results.append(i["title"])
  for i in range(len(top_news)):
    T = Text(root, height=2, width=100) 
    T.pack() 
    T.insert(END, results[i])
    print('\n')


   


      
if __name__ == '__main__': 
     
  # root=Tk()
   root.title("Top News App")
 
  
   head=Label(root,text="This Application is going display top 10 news around world",fg="blue")
   head.pack()
   button=Button(root,text="Get News",command=lambda :LatestNews())
   button.pack()
   clear=Button(root,text="Clear News",command=lambda :ClearNews())
   clear.pack()
  # button.grid(row=3,column=3)
   root.mainloop()
