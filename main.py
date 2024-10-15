# TictacToe code taken from: https://www.geeksforgeeks.org/tic-tac-toe-gui-in-python-using-pygame/
# Minimax code taken from: https://www.geeksforgeeks.org/finding-optimal-move-in-tic-tac-toe-using-minimax-algorithm-in-game-theory/
# Acessed on 10/10/2024
# No atribution listed
# CHANGELOG
# - changed mouse interaction to be mouse up and requires double click
# - Cleared events on game initiation 
# - Added a random move computer for single player
# - Combined minimax code with tictactoe
# - added evaluate function for minimax implementation 
# - adjusted check_win function for combatibility with minimax


import random
import pygame as pg
import sys
import time
from pygame.locals import *
 
# declaring the global variables
 
# for storing the 'x' or 'o'
# value as character
XO = 'x'
 
# storing the winner's value at
# any instant of code
winner = None
 
# to check if the game is a draw
draw = None
 
# to set width of the game window
width = 400
 
# to set height of the game window
height = 400
 
# to set background color of the
# game window
white = (255, 255, 255)
 
# color of the straightlines on that
# white game board, dividing board
# into 9 parts
line_color = (0, 0, 0)
 
# setting up a 3 * 3 board in canvas
board = [[None]*3, [None]*3, [None]*3]
 
 
# initializing the pygame window
pg.init()
 
# setting fps manually
fps = 30
 
# this is used to track time
CLOCK = pg.time.Clock()
 
# this method is used to build the
# infrastructure of the display
screen = pg.display.set_mode((width, height + 100), 0, 32)
 
# setting up a nametag for the
# game window
pg.display.set_caption("My Tic Tac Toe")
 
# loading the images as python object
initiating_window = pg.image.load("modified_cover.png")
x_img = pg.image.load("X_modified.png")
y_img = pg.image.load("o_modified.png")
 
# resizing images
initiating_window = pg.transform.scale(
    initiating_window, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(y_img, (80, 80))
 
 
def game_initiating_window():
 
    # displaying over the screen
    screen.blit(initiating_window, (0, 0))
 
    # updating the display
    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    # flush old events from window
    pg.event.clear() 
 
    # drawing vertical lines
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0),
                 (width / 3 * 2, height), 7)
 
    # drawing horizontal lines
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2),
                 (width, height / 3 * 2), 7)
    draw_status()
 
 
def draw_status():
 
    # getting the global variable draw
    # into action
    global draw
 
    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won !"
    if draw:
        message = "Game Draw !"
 
    # setting a font object
    font = pg.font.Font(None, 30)
 
    # setting the font properties like
    # color and width of the text
    text = font.render(message, 1, (255, 255, 255))
 
    # copy the rendered message onto the board
    # creating a small block at the bottom of the main display
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()
 
 
def check_win(ret_val = False):
    global board, winner, draw

    if(all([all(row) for row in board]) and winner is None):
        draw = True

    if ret_val:
        if draw:
            draw = None
            return True
        else:
            return False

    # checking for winning rows
    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0),
                         (0, (row + 1)*height / 3 - height / 6),
                         (width, (row + 1)*height / 3 - height / 6),
                         4)
            break
 
    # checking for winning columns
    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0),
                         ((col + 1) * width / 3 - width / 6, height), 4)
            break
 
    # check for diagonal winners
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
 
        # game won diagonally left to right
        winner = board[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)
 
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
 
        # game won diagonally right to left
        winner = board[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)
 
    draw_status()
 
 
def drawXO(row, col):
    global board, XO
 
    # for the first row, the image
    # should be pasted at a x coordinate
    # of 30 from the left margin
    if row == 1:
        posx = 30
 
    # for the second row, the image
    # should be pasted at a x coordinate
    # of 30 from the game line
    if row == 2:
 
        # margin or width / 3 + 30 from
        # the left margin of the window
        posx = width / 3 + 30
 
    if row == 3:
        posx = width / 3 * 2 + 30
 
    if col == 1:
        posy = 30
 
    if col == 2:
        posy = height / 3 + 30
 
    if col == 3:
        posy = height / 3 * 2 + 30
 
    # setting up the required board
    # value to display
    board[row-1][col-1] = XO
 
    if(XO == 'x'):
 
        # pasting x_img over the screen
        # at a coordinate position of
        # (pos_y, posx) defined in the
        # above code
        screen.blit(x_img, (posy, posx))
        XO = 'o'
 
    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()
 
 
def user_click():
    # get coordinates of mouse click
    x, y = pg.mouse.get_pos()
 
    # get column of mouse click (1-3)
    if(x < width / 3):
        col = 1
 
    elif (x < width / 3 * 2):
        col = 2
 
    elif(x < width):
        col = 3
 
    else:
        col = None
 
    # get row of mouse click (1-3)
    if(y < height / 3):
        row = 1
 
    elif (y < height / 3 * 2):
        row = 2
 
    elif(y < height):
        row = 3
 
    else:
        row = None
 
    # after getting the row and col,
    # we need to draw the images at
    # the desired positions
    if(row and col and board[row-1][col-1] is None):
        global XO
        drawXO(row, col)
        check_win()
        if not draw and not winner:
            computer_move()
# end user_click()
 
def evaluate (b):
    player = 'o'
    opponent = 'x'
    for row in range(0,3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == player:
                return 10
            elif b[row][0] == opponent:
                return -10
    for col in range(0,3):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            if b[0][col] == player:
                return 10
            elif b[0][col] == opponent:
                return -10
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[0][0] == player:
            return 10
        elif b[0][0] == opponent:
            return -10
    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[0][2] == player:
            return 10
        elif b[0][2] == opponent:
            return -10
        
    return 0

def minimax(board, depth, isMax) :  
    score = evaluate(board) 
  
    # If Maximizer has won the game return his/her  
    # evaluated score  
    if abs(score) == 10:  
        return score 
    if check_win(True) == True:
        return 0
  
    
  
    # If this maximizer's move  
    if isMax:      
        best = -1000 
  
        # Traverse all cells  
        for i in range(3) :          
            for j in range(3) : 
               
                # Check if cell is empty  
                if (board[i][j]== None) : 
                  
                    # Make the move  
                    board[i][j] = 'o'  
  
                    # Call minimax recursively and choose  
                    # the maximum value  
                    best = max( best, minimax(board, 
                                              depth + 1, 
                                              not isMax) ) 
  
                    # Undo the move  
                    board[i][j] = None
        return best 
  
    # If this minimizer's move  
    else : 
        best = 1000 
  
        # Traverse all cells  
        for i in range(3) :          
            for j in range(3) : 
               
                # Check if cell is empty  
                if (board[i][j] == None) : 
                  
                    # Make the move  
                    board[i][j] = 'x'  
  
                    # Call minimax recursively and choose  
                    # the minimum value  
                    best = min(best, minimax(board, depth + 1, not isMax)) 
  
                    # Undo the move  
                    board[i][j] = None
        return best 

def random_move():
    while True:
        row = random.randint(0,3)
        col = random.randint(0,3)
        if (row and col and board[row-1][col-1] is None):
            drawXO(row,col)
            check_win()
            break
#end random_move()

def computer_move():
    
    global XO
    best_val = -1000
    best_move = (-1,-1)

    # traverse all cells, evaluate minimax function for 
    # all empty cells. And return the cell with optimal
    # value.
    for row in range(1,4):
        for col in range(1,4):
            # check if cell is empty and valid
            if (board[row-1][col-1] is None):
                #make the move
                board[row-1][col-1] = XO
                # compute evaluation function for this move

                move_val = minimax(board, 0, False)
                # undo move
                board[row-1][col-1] = None

                # if the value of the current move is 
                # more than the best value, then update 
                # best
                if move_val > best_val:
                    best_move = (row, col)
                    best_val = move_val
    drawXO(best_move[0], best_move[1])
    check_win()
# end def computer_move():
 
def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_initiating_window()
    winner = None
    board = [[None]*3, [None]*3, [None]*3]
 
 
game_initiating_window()
 
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            user_click()
            if(winner or draw):
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)