"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"""

def alph(letter):
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	for n in range(len(alphabet)):
		if(alphabet[n]==letter): return n+1

def nameScore(name):
	tot=0
	for x in name:
                tot+=alph(x)
	return tot
	
total=0
wrd=""
place=1
with open('names.txt','r') as r:
    for line in sorted(r):
        for n in line:
                wrd+=n
        total+=(nameScore(wrd)*place)
        place+=1
        wrd=""
print(total)
