from curses import*
def a(s):
 curs_set(0);s.nodelay(1);u=v=.1;z=c=0;h,w=s.getmaxyx();p,q,f,a,b,d=w//2,h//2,s.addstr,round,range,'#';x,y=p,q;i=j=q
 while 1:
  k,x,y,m,n,o,t=s.getch(),x+u,y+v,i-5,i+5,j-5,j+5;s.clear();f(a(y),a(x),d)
  for e in b(-5,5):f(i+e,2,d);f(j+e,w-3,d);f(1,p-3,f'{z}:{c}')
  if k==49:break
  if(k==259)*o:j-=1
  if(k==258)*(h-t):j+=1
  if(k==119)*m:i-=1
  if(k==115)*(h-n):i+=1
  if y<0:y,v=0,-v
  elif~-h<y:y,v=~-h,-v
  if(x<3 and m<=y<n)|(x>w-4 and o<=y<t):u=-u
  elif x<2:x,y,c=p,q,-~c
  elif x>w-3:x,y,z=p,q,-~z
wrapper(a)
