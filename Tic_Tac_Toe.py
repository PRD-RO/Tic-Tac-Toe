from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Tic Tac Toe Game!')
root.geometry('370x460')

board = {i: '' for i in range(1, 10)}


Label(root, text='Welcome to The Game :)', bg='light green').grid(row=0, column=1, columnspan=3, pady=5)

Label(root, text='Play With:').grid(row=1, column=0)
v1 = IntVar()
Radiobutton(root, text='Computer', variable=v1, value=0).grid(row=1, column=1)
Radiobutton(root, text='Player', variable=v1, value=1).grid(row=1, column=2)

Label(root, text='Select:').grid(row=2, column=0)
v2 = IntVar()
Radiobutton(root, text='X', variable=v2, value=0).grid(row=2, column=1)
Radiobutton(root, text='O', variable=v2, value=1).grid(row=2, column=2)

Label(root, text='Start The Game?:').grid(row=3, column=0)
v3 = IntVar()
Radiobutton(root, text='Yes', variable=v3, value=0).grid(row=3, column=1)
Radiobutton(root, text='No', variable=v3, value=1).grid(row=3, column=2)


def wincheck(board, symbol):
    wins = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], 
        [1, 4, 7], [2, 5, 8], [3, 6, 9], 
        [1, 5, 9], [3, 5, 7]
    ]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
            return True
    return False

def Tiecheck(board):
    return all(board[i] != '' for i in board)

def disable():
    for i in buttons:
        buttons[i]['state'] = 'disabled'

def start():
    global currsymbol, Playwith
    Playwith = 'computer' if v1.get() == 0 else 'player'
    currsymbol = 'X' if v2.get() == 0 else 'O'
    startGame = 'yes' if v3.get() == 0 else 'no'

    for i in buttons:
        buttons[i]['text'] = ''
        buttons[i]['state'] = 'normal'
        board[i] = ''


    if Playwith=='computer' and startGame=='no':
      aiMove = Ai_move(board)
      if aiMove is not None:
         board[aiMove] = currsymbol
         buttons[aiMove]['text'] = currsymbol
         buttons[aiMove]['state'] = 'disabled'

      currsymbol = 'O' if currsymbol == 'X' else 'X'



    

def restart():
    global board
    board = {i: '' for i in range(1, 10)}
    for i in buttons:
        buttons[i]['text'] = ''
        buttons[i]['state'] = 'normal'

def Scour(board, ai_symbol, p_symbol):
    if wincheck(board, ai_symbol):
        return 1
    elif wincheck(board, p_symbol):
        return -1
    elif Tiecheck(board):
        return 0
    return None

def game_over(board):
    return wincheck(board, 'X') or wincheck(board, 'O') or Tiecheck(board)

def Ai_decition(board, depth, is_AI_turn):
    P_symbol = 'O' if currsymbol == 'X' else 'X'
    if game_over(board):
        return Scour(board, currsymbol, P_symbol)

    if is_AI_turn:
        result = -float('inf')
        for i in range(1, 10):
            if board[i] == '':
                copy_board = board.copy()
                copy_board[i] = currsymbol
                score = Ai_decition(copy_board, depth + 1, False)
                result = max(result, score)
        return result
    else:
        result = float('inf')
        for i in range(1, 10):
            if board[i] == '':
                copy_board = board.copy()
                copy_board[i] = P_symbol
                score = Ai_decition(copy_board, depth + 1, True)
                result = min(result, score)
        return result

def Ai_move(board):
    global currsymbol
    val = -float('inf')
    move = None
    for i in range(1, 10):
        if board[i] == '':
            copy_board = board.copy()
            copy_board[i] = currsymbol
            score = Ai_decition(copy_board, 0, False)
            if score > val:
                val = score
                move = i
    return move

def play(pos):
    global currsymbol
    if board[pos] == '':
        board[pos] = currsymbol
        buttons[pos]['text'] = currsymbol
        buttons[pos]['state'] = 'disabled'

        if wincheck(board, currsymbol):
            messagebox.showinfo('Winner', f'The winner is player {currsymbol}')
            disable()
            return
        if Tiecheck(board):
            messagebox.showinfo('Tie', 'Its a Tie')
            disable()
            return

        currsymbol = 'O' if currsymbol == 'X' else 'X'

#------------------------ Playing with computer:
        if Playwith == 'computer':
            aiMove = Ai_move(board)
            if aiMove is not None:
                board[aiMove] = currsymbol
                buttons[aiMove]['text'] = currsymbol
                buttons[aiMove]['state'] = 'disabled'

                if wincheck(board, currsymbol):
                    messagebox.showinfo('Winner', f'The winner is player {currsymbol}')
                    disable()
                    return
                if Tiecheck(board):
                    messagebox.showinfo('Tie', 'Its a Tie')
                    disable()
                    return

                currsymbol = 'O' if currsymbol == 'X' else 'X'



Button(root, text='Start', width=8, height=2, command=start).grid(row=4, column=3)
Button(root, text='Restart', width=8, height=2, command=restart).grid(row=8, column=3)

buttons = {}
for i in range(1, 10):
    buttons[i] = Button(root, text='',font=('Arial',20), width=5, height=2,bg='gray', command=lambda pos=i: play(pos))


positions = [
    (5, 1), (5, 2), (5, 3),
    (6, 1), (6, 2), (6, 3),
    (7, 1), (7, 2), (7, 3)
]
for i, pos in enumerate(range(1, 10)):
    buttons[pos].grid(row=positions[i][0], column=positions[i][1])

root.mainloop()
