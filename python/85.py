def findWays(maxXLen,maxYLen):
	ways=0
	for xLen in range(1,maxXLen+1):
		for yLen in range(1,maxYLen+1):
			ways+=(maxXLen-xLen+1)*(maxYLen-yLen+1)
			#print("X: "+str(xLen)+"\nY: "+str(yLen)+"\n")
	return(ways)

areaX=1
areaY=1
while(findWays(areaX,areaY)):
	print(str(areaX)+" "+str(areaY))
	areaY=1
	while(areaY<areaX):
		areaY+=1
	areaX+=1
print("X: "+str(areaX)+"\nY: "+str(areaY)) 
