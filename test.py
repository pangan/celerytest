from tasks import add
result = add.delay(3,6)
a=result.collect()
for key , res in a:
	print res