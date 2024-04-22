import random
l1=["rock","scissor","paper"]
while(1):
    Ucount=0
    Ccount=0
    Uchoice=int(input('''
    game start......
    press 1 (yes)
    press 2 (NO) | (Exit) 
    Press one of those options: '''))
    if Uchoice==1:
            for r in range(1,6):
                userinput=int(input('''
1 rock
2 scissor                                
3 paper  
Press one of these options:'''))
                if userinput==1:
                 Uchoice="rock"
                elif userinput==2:
                 Uchoice="scissor"
                elif userinput==3:
                 Uchoice="paper"
                Cchoice=random.choice(l1)      
                if Cchoice==Uchoice:
                  print("computer value:",Cchoice)
                  print("user value:",Uchoice)
                  print("Game Tie")
                  Ucount=Ucount+1
                elif(Uchoice=="rock" and Cchoice=="scissor") or(Uchoice=="paper" and Cchoice=="rock")or(Uchoice=="scissor" and Cchoice=="paper"):
                   print("computer value:",Cchoice)
                   print("User avlue:",Uchoice)
                   print("user wins")
                   Ucount=Ucount+1
                else:
                   print("computer value:",Cchoice)
                   print("user value:",Uchoice)
                   print("computer wins")
                   Ccount=Ccount+1
            if(Ucount==Ccount):
               print("Finally Game Tie")
               print("User score:",Ucount)
               print("Computer score:",Ccount)
            elif(Ucount>Ccount):
                print("Finally User wins")
                print("User score:",Ucount)
                print("Computer score:",Ccount)
            else:
               print("Finally Computer wins")
               print("User score:",Ucount)
               print("Computer score:",Ccount)   

       