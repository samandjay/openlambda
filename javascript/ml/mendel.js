// modes od mutation
//Observe that these are very simple mutation modes.
//Biologically one type of mutation is more common that other (transitions over trnasversions)

// random
let random = bases => Math.max(1, Math.floor(Math.random()*(bases+1)))
//cyclic
let cyclic = (b, bases) =>  (b + 1) % bases + 1

let mutate = (b, bases) => random( bases)
let mutateRow = (row, bases) => row.map( b => (b!=0)*mutate(b, bases))

let mutation = (data, bases) => data.map(r => mutateRow(r, bases))

let genome = {
	bases : 4,
	rows : 6,
	cols : 6,
	data :  [
		[1,1,0,0,0,0],
		[1,3,0,0,0,0],
		[0,0,3,2,0,0],
		[0,0,1,1,0,0],
		[0,0,0,0,1,1],
		[0,0,0,0,3,2]
	]
}

let generations = 100
for(let gen = 1; gen <= generations; gen++){
	genome.data = mutation( genome.data, genome.bases )
	console.log('generation',gen,'\n', genome )
}
