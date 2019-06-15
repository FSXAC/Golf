import curses,math
def c(s,r):
 s.clear()
 x,y,d,h,w=0,r,3-2*r,*s.getmaxyx()
 while x<y:
  a,b,x=int(x),int(y),x+1
  for p in zip([b,b,-b,-b,a,a,-a,-a],[a,-a,a,-a,b,-b,b,-b]):s.addstr(h//2+p[0],w//2+p[1],'*')
  if d>0:y,d=y-1,d+4*(x-y)+10
  else:d+=4*x+6
 s.refresh()
def m(s):
 s.nodelay(1)
 i=1
 while 1:
  if s.getch()==49:break
  c(s,9*math.sin(i)+15)
  i+=.1
curses.wrapper(m)
