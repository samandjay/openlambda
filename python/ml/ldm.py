import math

exponential = lambda a,b,n : a * math.exp(b*n)
fsin = lambda a,b,n : a * math.sin(2*math.pi*n*b)
fcos = lambda a,b,n : a * math.cos(2*math.pi*n*b)

class LDM:
	def __init__(self, l,d,m, oper):
		self.l, self.d, self.m, self.oper = l,d,m,oper
		self.scale = lambda a,b,n : a*b

	def apply(self, m, x, oper):
		return [sum([oper(row[i],x[i],i) for i in range(len(row))]) for row in m]

	def of(self, *argv):
		return self.apply(
				self.l,
				self.apply(
					self.d,
					self.apply(
						self.m,
						argv,
						self.scale
					),
					self.scale),
				self.oper
			)

m =  [
	[1,1,0,0,0,0],
	[1,3,0,0,0,0],
	[0,0,3,2,0,0],
	[0,0,1,1,0,0],
	[0,0,0,0,1,1],
	[0,0,0,0,3,2]
]

d =  [
	[1,1,0,0,0,0],
	[0,1,0,0,0,0],
	[0,0,1,1,0,0],
	[0,0,0,1,0,0],
	[0,0,0,0,1,1],
	[0,0,0,0,0,1]
]

l = [
	[1,1,0,0,0,0],
	[0,1,0,0,0,0],
	[0,0,1,1,0,0],
	[0,0,0,1,0,0],
	[0,0,0,0,1,1],
	[0,0,0,0,0,1]
]

print('Fourier sin')
print( LDM(l,d,m, fsin).of(1,1,0,1.4,2,4) )

print('\nFourier cos')
print( LDM(l,d,m, fcos).of(1,1,0,1.4,2,4) )

print('\nExponential')
print( LDM(l,d,m, exponential).of(1,1,0,1.4,2,4) )
