import curses
def a(s):
 curses.curs_set(0)
 s.nodelay(1)
 u=v=.1
 z=c=0
 h,w,f=s.getmaxyx(),s.addstr
 p,q=w//2,h//2
 x,y=p,q
 i=j=q
 while 1:
  k,x,y,m,n,o,t=s.getch(),x+u,y+v,i-5,i+5,j-5,j+5
  s.clear()
  f(round(y),round(x),'#')
  for e in range(m,n):f(e,2,'1')
  for e in range(o,t):f(e,w-3,'2')
  f(1,p-3,f'{z}:{c}')
  if k==49:break
  elif k==259 and o>1:j-=2
  elif k==258 and t<h:j+=2
  elif k==119 and m>1:i-=2
  elif k==115 and n<h:i+=2
  if y<0:y,v=0,-v
  elif y>=h-1:y,v=h-1,-v
  if(x<3 and m<=y<n)or(x>w-4 and o<=y<t):u=-u
  elif x<2:x,y,c=p,q,c+1
  elif x>w-3:x,y,z=p,q,z+1
curses.wrapper(a)
