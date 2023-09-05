import random
import sched
def game(n,m):
    if(n==1):
      print("the computer chose : " +"s")
    elif(n==2):
        print(  "the computer chose : " + "w")
    else:
        print( "the computer chose : "+ "g")


    if(n==1 and m=="s" ):
        print("tie")
    elif(n==2 and m=="w"):
        print("tie")
    elif(n==3 and m=="g"):
        print("tie")
    elif(n==1 and m=="w"):
        print(n ,"is the winner")
    elif(n==2 and m=="s"):
        print(m, "is the winner")
    elif(n==1  and m=="g"):
        print(m  ,"is the winner")
    elif(n==3 and m=="s"):
        print(n ,"is the winner")
    elif(n==2 and m=="g"):
        print(n," is the winner")
    else:
        print(m," is the winner")


a=input("choose between 's','w','g' : ")
b=random.randint(1,3)

game(b,a)