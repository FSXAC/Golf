import curses
def a(s):
 curses.curs_set(0)
 s.nodelay(1)
 u=v=.1
 z=c=0
 h,w=s.getmaxyx()
 p,q,f,a,b,d=w//2,h//2,s.addstr,round,range,'#'
 x,y=p,q
 i=j=q
 while 1:
  k,x,y,m,n,o,t=s.getch(),x+u,y+v,i-5,i+5,j-5,j+5
  s.clear()
  f(a(y),a(x),d)
  for e in b(m,n):f(e,2,d)
  for e in b(o,t):f(e,w-3,d)
  f(1,p-3,f'{z}:{c}')
  if k==49:break
  if k==259&o>1:j-=2
  if k==258&t<h:j+=2
  if k==119&m>1:i-=2
  if k==115&n<h:i+=2
  if y<0:y,v=0,-v
  elif~-h<y:y,v=~-h,-v
  if(x<3 and m<=y<n)|(x>w-4 and o<=y<t):u=-u
  elif x<2:x,y,c=p,q,-~c
  elif x>w-3:x,y,z=p,q,-~z
curses.wrapper(a)
