import random

board=[" " for x in range(10)]
def draw_board(board):
    print('\n')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def poscheck(board,pos):
    if board[pos]==' ':
        return True
    else:
        return False

def boardcheck(board):
    if board.count(' ') >0:
        return True
    else:
        return False

def check_winner(board,sym):
    if(board[1]==board[2]==sym and board[2]==board[3]==sym and board[1] != ' '):    
        return True   
    elif(board[4]==board[5]==sym and board[5]==board[6]==sym and board[4] != ' '):    
        return True    
    elif(board[7]==board[8]==sym and board[8]==board[9]==sym and board[7] != ' '):    
        return True
    elif(board[1]==board[4]==sym and board[4]==board[7]==sym and board[1] != ' '):    
        return True    
    elif(board[2]==board[5]==sym and board[5]==board[8]==sym and board[2] != ' '):    
        return True    
    elif(board[3]==board[6]==sym and board[6]==board[9]==sym and board[3] != ' '):
        return True    
    elif(board[1]==board[5]==sym and board[5]==board[9]==sym and board[5] != ' '):    
        return True    
    elif(board[3]==board[5]==sym and board[5]==board[7]==sym and board[5] != ' '):    
        return True 
    else:
        return False
        
def player_move(board):
    pl=True
    while pl:
        pos=int(input("Enter Position ->"))
        if (poscheck(board,pos)):
            board[pos]='x'
            pl=False
        else:
             print('!! space is occupied please enter other location !!')
      

def comp_move(board):
    pm = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['O', 'X']:
        for i in pm:
            boardCopy = board[:]
            boardCopy[i] = let
            if check_winner(boardCopy, let):
                move = i
                return move
    co = []
    for i in pm:
        if i in [1,3,7,9]:
            co.append(i)      
    if len(co) > 0:
        move=random.choice(co)
        return move
    if 5 in pm:
        move=5
        return move
    eo = []
    for i in pm:
        if i in [2,4,6,8]:
            eo.append(i)      
    if len(eo) > 0:
        move=random.choice(eo) 
    
    return move
    
print("Welcome to tic-tac-toe")
draw_board(board)
while (boardcheck(board)):
    if not(check_winner(board,'o')):
        player_move(board)
        draw_board(board)
    else:
        print("Computer Won")
        break
    
    if not(check_winner(board,'x')):
        move=comp_move(board)
        if move==0:
            print("Game tie")
        else:
            board[move]='o'
            print("\n__________________\n")
            draw_board(board)
    else:
        print("Player won")
         
