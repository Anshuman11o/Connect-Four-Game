# Author   : Anshuman Agarwal
# Email    : anagarwal@umass.edu
# Spire ID : 34157323

def make_empty_board(nrows,ncols):
    num_col = '.'*ncols
    board_list = list([num_col]*nrows)
    return board_list

#print(make_empty_board(6, 4))

def print_board(list_of_strings):
    for rows in range(0,len(list_of_strings)):
        count = 0
        for cols in range(0,len(list_of_strings[rows])):
            if cols==len(list_of_strings[rows])-1:
                if (list_of_strings[rows][cols]=='X'):
                  spot = ' X '
                  print(spot,end="")
                elif (list_of_strings[rows][cols]=="O"):
                  spot = ' O '
                  print(spot,end="")
                elif (list_of_strings[rows][cols]=='.'):
                  spot = '   '
                  print(spot,end="")
            elif cols != len(list_of_strings[rows]) - 1:
                if list_of_strings[rows][cols] == 'X':
                  spot = ' X '
                  print(spot + '|', end="")
                elif list_of_strings[rows][cols] == 'O':
                  spot = ' O '
                  print(spot + '|', end="")
                elif list_of_strings[rows][cols] == '.':
                  spot = '   '
                  print(spot + '|', end="")
            count += 1
        print()    
        if rows== len(list_of_strings)-1:
            print("")
        else:
            print("---+"*(count-1)+'---')     

#print_board([".......", ".......", "..O....", "..OX...", ".OXOX..",".OXXOXX"])
#print_board(make_empty_board(5, 6))

def verify_board(list_of_strings):
   num_O = 0
   num_X = 0
   disc = False
   T_F = True
   for rows in range(0,len(list_of_strings)):
        for cols in range(0,len(list_of_strings[rows])):
           if list_of_strings[rows][cols]=='O':
              num_O += 1
              disc = True
           elif list_of_strings[rows][cols]=='X':
              num_X += 1
              disc = True
           elif list_of_strings[rows][cols]=='.':
              T_F = True

           if rows!=len(list_of_strings)-1:
             if disc and (list_of_strings[rows+1][cols]=='.'): #checks wether there is an empty spot below a filled spot or not
                  return False
   
   if ((num_O-num_X)>=2) or ((num_X-num_O)>=2):
              return False       
    
   return T_F
              
#board = [".......", ".......", "..O....", "..OX...", ".O.OX..",".O.XOX."]
#print(verify_board(board))
#board = ["X......", ".......", "..O....", "..OX...", ".O.OX..",".O.XOXX"]
#print(verify_board(board))
#print(verify_board(['...OXXXO', '...XOXX.', '.O.XOXX.', '.XO.O...']))

def verify_move(list_of_strings, chosen_col):
   if (chosen_col <0) or (chosen_col>=(len(list_of_strings[0]))):
      return False
   elif (list_of_strings[0][chosen_col])!= '.':
      return False
   else:
      return True

#board = ["..O....", "..X....", "..O....", "..OX...", ".OXOX..",".OXXOX."] 
#print(verify_move(board, 2)) 
#print(verify_move(board, 1))
#print(verify_move(board, 7))

def update_board(list_of_strings, chosen_col, disc_type):
   loc_row=None
   for row in range(len(list_of_strings)-1,-1,-1):
      if (list_of_strings[row][chosen_col])=='.':
         loc_row = row
         break
      else:
         continue
   new_list = list(list_of_strings[loc_row])
   new_list[chosen_col] = disc_type
   list_of_strings[loc_row] = "".join(new_list)
   return list_of_strings
   
#board = [".......", ".......", "..O....", "..OX...", ".OXOX..",".OXXOX."] 
#print(update_board(board, 0, 'X'))
#board = [".......", ".......", "..O....", "..OX...", ".OXOX..",".OXXOX."]
#print(update_board(board, 2, 'O')) 

def has_won(list_of_strings, col_index):
   row_top = None
   disc = None
   flag1 = False
   flag2 = False
   flag3 = False
   flag4 = False
   count = 0
   for row in range(0,len(list_of_strings)):
      if (list_of_strings[row][col_index])=='O' or (list_of_strings[row][col_index])=='X':
         row_top = row
         disc = list_of_strings[row][col_index]
         break
   for check in range(row_top,len(list_of_strings)):
      if (list_of_strings[check][col_index])== disc:
         count += 1
      else:
         break

   if count>=4:
      flag1 = True
   #check for row starts here
   count = 0
   for check_col in range(col_index,len(list_of_strings[row_top])):
      if (list_of_strings[row_top][check_col])== disc:
         count += 1
      else:
         break
   if count>=4:
      flag2 = True
   else:
      for check_col1 in range(col_index-1,-1, -1):
          if (list_of_strings[row_top][check_col1])== disc:
             count +=1
          else:
             break
   if count>=4:
      flag2 = True
   else:
      flag2 = False
   #check for diagnol starts here
   x = 0
   count=0  
   for LL_row in range(row_top,len(list_of_strings)):
        if ((col_index-x>=0) and (list_of_strings[LL_row][col_index-x]==disc)):
            count+=1
            x+=1
        else:
            break
          
   x = 1
   for UR_row in range(row_top-1,-1,-1):
        if (((x+col_index)<len(list_of_strings[UR_row])) and (list_of_strings[UR_row][col_index+x]==disc)):
            count+=1
            x+=1
        else:
            break
       
   if count>=4:
      flag3 = True
   x=0
   count = 0
   for LR_row in range(row_top,len(list_of_strings)):
        if ((x+col_index<len(list_of_strings[LR_row])) and (list_of_strings[LR_row][col_index+x]==disc)):
            count+=1
            x+=1
        else:
            break
             
   x=1
   for UL_row in range(row_top-1,-1,-1):
        if ((col_index-x>=0) and (list_of_strings[UL_row][col_index-x]==disc)):
            count+=1
            x+=1
        else:
            break
             
   if count>=4:
      flag4 = True

   if flag1 or flag2 or flag3 or flag4:
      #print(flag1, flag2,flag3,flag4)
      return True
   else:
      return False

#board = [".......", ".......", "..OO...", ".XOX...", ".OXOX..","OOXXOXX"]
#print(has_won(board, 3))
#print(has_won(['...O...O', 'O.XX.X.X', 'OXOX.XOO', 'XXOXXOOX', 'XOOOXOXO'], 2))

