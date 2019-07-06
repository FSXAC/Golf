from curses import *
import datetime
def m(S):
 curs_set(0);p=n=b=s=0;c=S.clear;f=S.addstr;c();f(0,0,'Tap any key to start');
 while 1:
  k=S.getch();p,n=n,datetime.datetime.now()
  if k==27:break
  if p and n:
   d=n-p;B=60/d.total_seconds()
   if b:w=1/-~s;b=b*(1-w)+B*w;c();f(0,0,f'BPM: {round(b)}')
   else:b=B
  s+=1
wrapper(m)
