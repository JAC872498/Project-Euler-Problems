def perf(n):#False==not abundant, True==abundant
	if(n%2!=0 or n%3!=0): return False
	total=0
	for x in range(n):
		if(x>n-x):
			return False
		if(n%(x+1)==0):
			total+=x+1
			if(total>n):
				return True
	return False
	 
total=0
for m in range(20162):
	total+=(m+1)
	print(m)
	for n in range(m+1):
		if(perf((m+1)-(n+1))==True and perf(n+1)==True):
			total-=(m+1)
			break
print(total)