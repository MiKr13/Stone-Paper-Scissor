from random import randint

l = ['stone', 'paper', 'scissor']
choice=""
print("\nWelcome to Stone, Paper, Scissor\n");
print("\nInstructions:\nEnter 'stone', 'paper', 'scissor' pr 'exit' only(Without quotes)\n")

def play(c):
    v= randint(0, 2)
    print("\nComputer's Choice: "+l[v])
    if(l[v]=='stone' and c=='scissor') and (l[v]=='stone' and c!='paper'):
        print("\nYOU LOST!")
    elif(l[v]=='paper' and c=='stone') and (l[v]=='paper' and c!='scissor'):
        print("\nYOU LOST!")
    elif(l[v]=='scissor' and c=='paper') and (l[v]=='scissor' and c!='stone'):
        print("\nYOU LOST!")
    elif(l[v]==c):
        print("\nDRAW!")
    else:
        print("\nYOU WON!")

while(choice[:]!='exit'):
	c= input("\nEnter your choice:")
	print("\nYour choice: "+c)
	if(c in l):
	    play(c.lower())
	elif(c=="exit"):
		exit()
	else:
	    print("\nEnter Stone, Paper, Scissor only!")
