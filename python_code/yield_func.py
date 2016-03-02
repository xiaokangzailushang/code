def yield_fun():
	for i in range(10):
		yield i

	for m in range(11,20):
		yield m

mygenerator=yield_fun()
print mygenerator,"\n"
print next(mygenerator)
print next(mygenerator)
