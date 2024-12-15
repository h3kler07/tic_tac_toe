import os
placeholder=['1','2','3','4','5','6','7','8','9']
occupied = []
def clear():
   os.system('cls')
def board():
   
   board= f'''
   {placeholder[0]} | {placeholder[1]} | {placeholder[2]}
   --|---|--
   {placeholder[3]} | {placeholder[4]} | {placeholder[5]}
   --|---|--
   {placeholder[6]} | {placeholder[7]} | {placeholder[8]}
   '''
   print(board)


def check_win(player):
   #TOP TO BOTTOM
   if placeholder[0]==placeholder[3]==placeholder[6]:
      clear()
      board()
      print(placeholder[0]+" WINS!")
      
      exit()
   elif placeholder[1]==placeholder[4]==placeholder[7]:
      clear()
      board()
      print(placeholder[1]+" WINS!")
      exit()
   elif placeholder[2]==placeholder[5]==placeholder[8]:
      clear()
      board()
      print(placeholder[2]+" WINS!")
      exit()
   elif len(occupied)==9:
      clear()
      board()
      print("ITS A DRAW!")
      exit()

   


   #LEFT TO RIGHT
   elif placeholder[0]==placeholder[1]==placeholder[2]:
      clear()
      board()
      print(placeholder[0]+" WINS!")
      exit()
   elif placeholder[3]==placeholder[4]==placeholder[5]:
      clear()
      board()
      print(placeholder[3]+" WINS!")
      exit()
   elif placeholder[6]==placeholder[7]==placeholder[8]:
      clear()
      board()
      print(placeholder[6]+" WINS!")
      exit()
   

   #DIAGONALS
   elif placeholder[0]==placeholder[4]==placeholder[8]:
      clear()
      board()
      print(placeholder[0]+" WINS!")
      exit()
   elif placeholder[2]==placeholder[4]==placeholder[6]:
      clear()
      board()
      print(placeholder[2]+" WINS!")
      exit()
   else:
      if player == 'X':
         clear()

         Yplay()
      elif player == 'O':
         clear()
 
         Xplay()
      else:
         print("ERROR")
         exit()

def Xplay():
   board()
   num = int(input("X's TURN => "))
   if str(num) not in occupied:
      occupied.append(num)
      placeholder[num-1] = 'X'
      check_win('X')

def Yplay():
   board()
   num = int(input("O's TURN => "))
   if str(num) not in occupied:
      occupied.append(num)
      placeholder[num-1] = 'O'
      check_win('O')
Xplay()


