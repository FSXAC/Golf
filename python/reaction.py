from curses import*
import datetime,random
def m(s):
 s.nodelay(1);curs_set(0);t,f,D,c=[],s.addstr,datetime.datetime,s.clear;x=i=a=b=0
 while 1:
  k=s.getch();K=k-46
  if k==27:break
  if x==0:
   c();f(1,1,'Use period key to test')
   if t:f(2,1,f'ms:  {", ".join([str(q)for q in t])}');f(3,1,f'avg: {round(sum(t)/len(t))}')
   if K==0:i,x=random.randint(15e3,2e5),1;c();f(1,1,'Wait')
  elif x==1:
   if K==0:x=0
   if i:i-=1
   elif i==0:c();f(1,1,'PRESS',10485760);x,a=2,D.now()
  elif(x==2)&(K==0):b=D.now();d,x=b-a,0;t+=[round(d.total_seconds()*1e3)]
wrapper(m)
