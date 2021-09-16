let symbols = (size,fidx) => `(select 0 as x${fidx} union ` + Array.from({length: size-1}, (_,idx) => `select ${idx + 1}`).join(' union ') + ') d'
let fields = (size, sep, alphabetSize) => Array.from({length: size}, (_,idx) => symbols(alphabetSize,idx) + idx).join(sep)
let window = (size, start) => ` limit ${size} offset ${start}`

let machine = (width, height, start, sep, alphabetSize) => 'select * from\n' + fields(width, sep, alphabetSize) + '\n'  + window(height, start)


let [width, height, start, sep, alphabetSize] = [3, 1024, 0, ',\n',10]

console.log( machine( width, height, start, sep, alphabetSize ) )
