import curses,math
def c(s,r):
 h,w=s.getmaxyx()
 s.clear()
 def f(x,y):
  for p in zip([y,y,-y,-y,x,x,-x,-x],[x,-x,x,-x,y,-y,y,-y]):s.addstr(h//2+p[0],w//2+p[1],'*')
 x,y,d=0,r,3-2*r
 while x<y:
  f(int(x),int(y))
  x+=1
  if d>0:y,d=y-1,d+4*(x-y)+10
  else:d+=4*x+6
 s.refresh()
def m(s):
 s.nodelay(1)
 i=1
 while i:
  if s.getch()==49:break
  c(s,9*math.sin(i)+15)
  i+=.1
curses.wrapper(m)
