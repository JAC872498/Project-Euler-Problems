"""In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD		2C 3S 8S 8D TD		Player 2
		Pair of Fives		Pair of Eights
 	
2	 	5D 8C 9S JS AC		2C 5C 7D 8S QH		Player 1
		Highest card Ace	Highest card Queen	
 	
3	 	2D 9C AS AH AC		3D 6D 7D TD QD		Player 2
		Three Aces		Flush with Diamonds
 	
4	 	4D 6S 9H QH QC		3D 6D 7H QD QS		Player 1
		Pair of Queens		Pair of Queens
		Highest card Nine	Highest card Seven
 	
5	 	2H 2D 4C 4D 4S		3C 3D 3S 9S 9D		Player 1
		Full House		Full House
		With Three Fours	with Three Threes
 	
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?"""

def getHand(pS,pC):
	score=[1,0,0,0,0,0]
	spot=1
	if(5 in pS):
		
		if(6>score[0]):#Flush
			score=[6,0,0,0,0,0]
			spot=1
			for n in range(len(pC),0,-1):
				if(pC[n-1]>0):
					score[spot]=n-1
					spot+=1:#Flush
					
		if(pC[10]==1 and pC[11]==1 and pC[12]==1 and pC[13]==1 and pC[14]==1):#Royal Flush
			score[0]=max(score[0],10)#Royal Flush
			
		for n in range(0,len(pC)-4):
			if(pC[n]==1 and pC[n+1]==1 and pC[n+2]==1 and pC[n+3]==1 and pC[n+4]==1):
				if(9>score[0]):#Straight Flush
					score=[9,0,0,0,0,0]
					spot=1
					for n in range(len(pC),0,-1):
						if(pC[n-1]>0):
							score[spot]=n-1
							spot+=1#Straight Flush
	for n in pC:
		if(n==4):
			if(8>score[0]):#Four of a Kind
				score=[8,0,0,0,0,0]
				for n in range(len(pC)):
					if(pC[n]==4):
						score[1]=n
					if(pC[n]==1):
						score[2]=n#Four of a Kind
						
		if(n==3):
			if(4>score[0]):#Three of a Kind
				score=[4,0,0,0,0,0]
				for n in range(len(pC)):
					if(pC[n]==3):
						score[1]=n
					if(pC[n]==1 and score[2]==0):
						score[2]=n
					else:
						score[3]=n#Three of a Kind
						
			for n2 in pC:
				if(n2==2):
					if(7>score[0]):#Full House
						score=[7,0,0,0,0,0]
						for n in range(len(pC)):
							if(pC[n]==3):
								score[1]=n
							if(pC[n]==2):
								score[2]=n#Full House
								
		if(n==2):
			n1=pC.index(2)
			for n2 in range(len(pC),0,-1):
				if(pC[n2-1]==2 and n1!=n2-1):
					if(3>score[0]):#Two Pairs
						spot=3
						score=[3,0,0,0,0,0]
						for n in range(len(pC),0,-1):
							if(pC[n-1]==2 and score[1]==0):
								score[1]=n
							elif(pC[n-1]==2):
								score[2]=n
							if(pC[n-1]==1):
								score[spot]=n
								spot+=1:#Two Pairs
									
			if(2>score[0]):#One Pair
				spot=2
				score=[2,0,0,0,0,0]
				for n in range(len(pC),0,-1):
					if(pC[n-1]==2):
						score[1]=n-1
					if(pC[n-1]==1):
						score[spot]=n-1
						spot+=1#One Pair
						
	for n in range(len(pC)-4):
		if(pC[n]==1 and pC[n+1]==1 and pC[n+2]==1 and pC[n+3]==1 and pC[n+4]==1):
			if(5>score[0]):#Straight
				score=[5,0,0,0,0,0]
				score[1]=n+4
				
	if(score[0]!=1):
		return(score)
	spot=1
	for n in range(len(pC),0,-1):
		if(pC[n-1]>0):
			score[spot]=n-1
			spot+=1
	return(score)

def getWinner(n1,n2,p1C,p2C):
	for n in range(len(n1)):
		if(n1[n]>n2[n]):
			return(True)
		if(n2[n]>n1[n]):
			return(False)

suits=["D","C","H","S"]
cards=[" "," ","2","3","4","5","6","7","8","9","T","J","Q","K","A"]
p1Score=0
with open('poker.txt','r') as r:
	for line in r:
		p1S=[0,0,0,0]#Diamond, club, heart, spade
		p1C=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#empty,empty,2,3,4,5,6,7,8,9,10,jack,queen,king,Ace
		p2S=[0,0,0,0]
		p2C=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		p1=list(line[:14])
		p2=list(line[15:29])
		for n in range(1,len(p1),3):
			p1S[suits.index(p1[n])]+=1
			p1C[cards.index(p1[n-1])]+=1
			p2S[suits.index(p2[n])]+=1
			p2C[cards.index(p2[n-1])]+=1
		if(getWinner(getHand(p1S,p1C),getHand(p2S,p2C),p1C,p2C)):
			p1Score+=1
print(p1Score)
