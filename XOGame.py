import random 

def Display(OXList):
    print(OXList[0] +" | "+ OXList[1] +" | " + OXList[2])
    print('__________')
    print(OXList[3] +" | "+ OXList[4] +" | " + OXList[5])
    print('__________')
    print(OXList[6] +" | "+ OXList[7] +" | " + OXList[8])

def Avalible(OXList,position):
   if OXList[position]==" ":
      return True
   else: 
     return False

def Play(OXList,OX):
  while True:
      try:
          inp=int(input("Enter a Number 1-9: "))-1
          if inp < 0 or inp > 8:
             print("Choose an appropriate position as shown above")
          elif not Avalible(OXList,inp):
             print("This position is full. choose Another")
          else: 
             OXList[inp]=OX
             break
      except ValueError:
          print("Enter a valid number")

def computer_play(OXList,computer) :   
   avalible_position=[i for i in range(9) if Avalible(OXList,i)]
   choic=random.choice(avalible_position)
   OXList[choic]=computer

def SetUP():
  mode=input("Choose Who You Want To Play With(Computer Or Player): ").strip().lower()
  OX=input("Choose X Or O ").upper()
  while OX not in["X","O"]:
     OX=input("Wrong choose only X or O: ").upper()
  if OX =="X":
    computer="O"
  else:
    computer="X"
  Start=input("Do You Want To Start? Y|N ").strip().lower()
  player_start= True if Start=="y" else False
  return mode,OX,computer,player_start
   
def CheckWin(OXList,OX):
  WinPosepilities=[ [0,3,6],[1,4,7],[2,5,8],
                   [0,1,2],[3,4,5],[6,7,8] ,
                   [0,4,8],[2,4,6]] 
  for i in WinPosepilities:
    if OXList[i[0]]== OXList[i[1]]== OXList[i[2]]== OX:
      return True
  return False

def CheckTie(OXList):
  return " " not in OXList


while True:
    OXList=[" "," "," ",
            " "," "," ",
            " "," "," "]

    mode,OX,computer,player_start=SetUP()
    print("You can choose number as below to enter your letter in")
    print(OXList[0] +"1  | "+ OXList[1] +"2  | 3 " + OXList[2])
    print('___________________')
    print(OXList[3] +"4  | "+ OXList[4] +"5  | 6 " + OXList[5])
    print('___________________')
    print(OXList[6] +"7  | "+ OXList[7] +"8  | 9 " + OXList[8])

    Display(OXList)

    turn="player" if player_start else "computer"
    while True:
      Display(OXList)
      if turn == "player":
        Play(OXList,OX)
        if CheckWin(OXList,OX):
          Display(OXList)
          print("Player Won")
          break
        turn= "computer" if mode=="computer" else "player2"
      elif turn =="computer":
        computer_play(OXList,computer)
        if CheckWin(OXList,computer):
          Display(OXList)
          print("Computer Won")
          break
        turn="player"
      elif turn=="player2":
        Play(OXList,computer)
        if CheckWin(OXList,computer):
          Display(OXList)
          print("Second player won ")
          break
        turn="player"
      if CheckTie(OXList):
        Display(OXList)
        print("its a tie")
        break
    
    # ---------------- Play Again? ----------------
    again = input("Do you want to play again? (Y/N): ").strip().lower()
    if again != "y":
        print("Game Over. Thanks for playing!")
        break
