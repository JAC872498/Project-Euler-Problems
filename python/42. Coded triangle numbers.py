"""The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?"""

def word(str):
	tot=0
	alphabet=['"',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	for l in str:
		for n in range(len(alphabet)):
			if(alphabet[n]==l): tot+=n
	return tot
tris=[]
wrd=""
tot=0
for num in range(1,19):
	tris.append((num/2)*(num+1))
with open("words.txt","r") as f:
	for x in f.readline():
		if(x!=","):
			wrd=wrd+x
		else:
			if(word(wrd) in tris):
				tot+=1
			wrd=""
print(tot)
