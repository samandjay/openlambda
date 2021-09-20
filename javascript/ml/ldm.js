let exponential = (a,b,n) => a * Math.exp(b*n)
let fsin = (a,b,n) => a * Math.sin(2*Math.PI*n*b)
let fcos = (a,b,n) => a * Math.cos(2*Math.PI*n*b)

class LDM{
	constructor(l, d, m, oper){
		this.l = l
		this.d = d
		this.m = m
		this.oper = oper
		this.scale = (a,b,n) => a*b
	}

	apply(m, x, oper){
		return m.map( row => row.map((v,i) => oper(v,x[i],i) ).reduce((acc,c) => acc + c,0) )
	}

	of(){
		return	this.apply(
				this.l,
				this.apply(
					this.d,
					this.apply(
						this.m,
						arguments,
						this.scale),
					this.scale),
				this.oper)
	}
}



let m =  [
	[1,1,0,0,0,0],
	[1,3,0,0,0,0],
	[0,0,3,2,0,0],
	[0,0,1,1,0,0],
	[0,0,0,0,1,1],
	[0,0,0,0,3,2]
]

let d =  [
	[1,1,0,0,0,0],
	[0,1,0,0,0,0],
	[0,0,1,1,0,0],
	[0,0,0,1,0,0],
	[0,0,0,0,1,1],
	[0,0,0,0,0,1]
]

let l = [
	[1,1,0,0,0,0],
	[0,1,0,0,0,0],
	[0,0,1,1,0,0],
	[0,0,0,1,0,0],
	[0,0,0,0,1,1],
	[0,0,0,0,0,1]
]

console.log('Fourier sin')
console.log( new LDM(l,d,m, fsin).of(1,1,0,1.4,2,4).join('\n') )

console.log('\nFourier cos')
console.log( new LDM(l,d,m, fcos).of(1,1,0,1.4,2,4).join('\n') )

console.log('\nExponential')
console.log( new LDM(l,d,m, exponential).of(1,1,0,1.4,2,4).join('\n') )

