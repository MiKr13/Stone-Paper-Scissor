from random import randint

l = ['stone', 'paper', 'scissor']
print("Welcome to Stone, Paper, Scissor\n");
print("\nInstructions:\nEnter 'stone', 'paper' or 'scissor' only(Without quotes)\n")

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

c = input("Enter your choice:")
print("\nYour choice: "+c)
if(c in l):
    play(c.lower())
else:
    print("Enter Stone, Paper, Scissor only!")