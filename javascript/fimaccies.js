let fimacci = (x,y) => [y, x + y]

let fimaccies = (x,y,n, sink) => {
	while(n-->=0){
		[x,y] = fimacci(x,y)
		sink(y)
	}
}

fimaccies(-1,1, process.argv[2], f => console.log(f))
