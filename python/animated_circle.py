import curses,math
def m(s):
 s.nodelay(1);i=1
 while 1:
  if s.getch()==49:break
  r=9*math.sin(i)+15;s.clear();h,w=s.getmaxyx();x,y,d=0,r,3-2*r
  while x<y:
   a,b=int(x),int(y);x+=1
   for p in zip([b,b,-b,-b,a,a,-a,-a],[a,-a,a,-a,b,-b,b,-b]):s.addstr(h//2+p[0],w//2+p[1],'*')
   if d>0:d+=4*(x-y)+10;y-=1
   else:d+=4*x+6
  s.refresh();i+=.1
curses.wrapper(m)
