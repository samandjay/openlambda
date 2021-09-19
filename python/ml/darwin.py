from random import uniform

express = lambda row : [(b!=0)*uniform(.01,1) for b in row ]
expression = lambda data : [express(row) for row in data]

class Genome:
	def __init__(self, **entries):
		self.__dict__.update(entries)

gdata = {
	'bases': 4,
	'rows': 6,
	'cols': 6,
	'data' :  [
		[1,1,0,0,0,0],
		[0,1,0,0,0,0],
		[0,0,1,1,0,0],
		[0,0,0,1,0,0],
		[0,0,0,0,1,1],
		[0,0,0,0,0,1]
	]
}

genome = Genome(**gdata)

generations = 10
for gen in range(1, generations):
	print('generation {}\n{}'.format(gen, expression(genome.data)) )
