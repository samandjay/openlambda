import sys

fimacci = lambda x,y : (y, x+y)

def fimaccies (x, y, n):
	while n>=0:
		x,y = fimacci(x,y)
		n -= 1

		print(y)

n = int(sys.argv[1])
fimaccies(-1,1,n)
