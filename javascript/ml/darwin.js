let express = row => row.map(b => (b!=1)*Math.random())
let expression = data => data.map(row => express(row))

let genome = {
	bases : 4,
	rows : 6,
	cols : 6,
	data :  [
		[1,1,0,0,0,0],
		[0,1,0,0,0,0],
		[0,0,1,1,0,0],
		[0,0,0,1,0,0],
		[0,0,0,0,1,1],
		[0,0,0,0,0,1]
	]
}

let generations = 100
for(let gen = 1; gen <= generations; gen++){
	console.log('generation',gen,'\n', expression( genome.data ) )
}
