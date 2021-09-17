##let symbols = (size,fidx) => `(select 0 as x${fidx} union ` + Array.from({length: size-1}, (_,idx) => `select ${idx + 1}`).join(' union ') + ') d'
##let fields = (size, sep, alphabetSize) => Array.from({length: size}, (_,idx) => symbols(alphabetSize,idx) + idx).join(sep)
##let window = (size, start) => ` limit ${size} offset ${start}`

##let machine = (width, height, start, sep, alphabetSize) => 'select * from\n' + fields(width, sep, alphabetSize) + '\n'  + window(height, start)


##let [width, height, start, sep, alphabetSize] = [8, 1024, 0, ',\n',2]

##console.log( machine( width, height, start, sep, alphabetSize ) )


symbols = lambda size, fidx : '(select 0 as x{} union '.format(fidx) + ' union '.join(['select {}'.format(i+1) for i in range(size-1)])  + ') d'
fields = lambda size, sep, alphabetSize : sep.join([ '{}{}'.format(symbols(alphabetSize, i), i) for i in range(size) ])
window = lambda size, start : ' limit {} offset {}'.format(size, start)
machine = lambda width, height, start, sep, alphabetSize : 'select * from\n' + fields(width, sep, alphabetSize) + '\n'  + window(height, start)


width, height, start, sep, alphabetSize = 8, 1024, 0, ',\n',2

print( machine( width, height, start, sep, alphabetSize ) )
