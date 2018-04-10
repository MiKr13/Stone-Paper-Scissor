from random import randint

print("Welcome to Stone, Paper, Scissor");
def play(c):
    v= randint(0, 2)
    l = ['Stone', 'Paper', 'Scissor']
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

c = input("Enter your choice: ")
print("\nYour choice: "+c)
verify=str(type(c))
if(verify[8:11]=="str"):
    play(c)
else:
    print("Enter Stone, Paper, Scissor only!")
