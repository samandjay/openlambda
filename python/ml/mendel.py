from random import randint

# modes od mutation
# Observe that these are very simple mutation modes.
# Biologically one type of mutation is more common that other (transitions over trnasversions)

#random
random = lambda bases : randint(1, bases)
#cyclic
cyclic = lambda b, bases : (b + 1) % bases + 1

mutate = lambda b, bases : random( bases )
mutateRow = lambda row, bases : [(b!=0) * mutate(b,bases) for b in row]

mutation = lambda data, bases : [mutateRow(r, bases) for r in data]

class Genome:
	def __init__(self, **entries):
		self.__dict__.update(entries)

gdata = {
	'bases': 4,
	'rows': 6,
	'cols': 6,
	'data' :  [
		[1,1,0,0,0,0],
		[1,3,0,0,0,0],
		[0,0,3,2,0,0],
		[0,0,1,1,0,0],
		[0,0,0,0,1,1],
		[0,0,0,0,3,2]
	]
}

genome = Genome(**gdata)

generations = 10
for gen in range(1, generations):
	genome.data = mutation( genome.data, genome.bases )
	print('generation {}\n{}'.format(gen, genome.data) )
