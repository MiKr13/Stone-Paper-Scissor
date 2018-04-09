from random import randint

print("Welcome to Stone, Paper, Scissor");
def play(c):
    v= randint(0, 2)
    l = ['Stone', 'Paper', 'Scissor']
    print("Computer's Choice: "+l[v])
    if(l[v]=='Stone' and c=='Scissor') and (l[v]=='Stone' and c!='Paper'):
        print("YOU LOST!")
    elif(l[v]=='Paper' and c=='Stone') and (l[v]=='Paper' and c!='Scissor'):
        print("YOU LOST!")
    elif(l[v]=='Scissor' and c=='Paper') and (l[v]=='Scissor' and c!='Stone'):
        print("YOU LOST!")
    elif(l[v]==c):
        print("DRAW!")
    else:
        print("YOU WON!")

c = input("Enter your choice: ")
print("Your Choice: "+c)
if(type(c)=="<class 'str'>"):
    play(c)
else:
    print("Enter Stone, Paper or Scissor only!")