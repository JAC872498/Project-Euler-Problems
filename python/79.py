"""A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length."""

values=[]
file=open("keylog.txt")#individual 3-len codes
for n in file.read().split("\n"):
	if(n+"" not in values):#Doesn't add dups
		values.append(n+"")
file.close()

while(len(values)>1):
	values=combine(values)
print(values)
print(len(values[0]))