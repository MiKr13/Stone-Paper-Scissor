from random import randint

l = ['Stone', 'Paper', 'Scissor']
print("Welcome to Stone, Paper, Scissor\n");
print("\nInstructions:\nEnter Stone for 'stone', Paper for 'paper' and Scissor for 'scissor'\n")

def play(c):
    v= randint(0, 2)
    print("\nComputer's Choice: "+l[v])
    if(l[v]=='Stone' and c=='Scissor') and (l[v]=='Stone' and c!='Paper'):
        print("\nYOU LOST!")
    elif(l[v]=='Paper' and c=='Stone') and (l[v]=='Paper' and c!='Scissor'):
        print("\nYOU LOST!")
    elif(l[v]=='Scissor' and c=='Paper') and (l[v]=='Scissor' and c!='Stone'):
        print("\nYOU LOST!")
    elif(l[v]==c):
        print("\nDRAW!")
    else:
        print("\nYOU WON!")

c = input("Enter your choice:")
print("\nYour choice: "+c)
if(c in l):
    play(c)
else:
    print("Enter Stone, Paper, Scissor only!")