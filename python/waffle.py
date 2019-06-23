import sys
r=int(sys.argv[1])
k=range(-r,r)
for y in k:
 o=''
 for x in k:
  o+='#'if x*x+y*y<r*r else' '
 print(o)
