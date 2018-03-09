import pygame, sys 
from pygame.locals import* 
pygame.init() 

screen = pygame.display.set_mode((500, 350)) 
pygame.display.set_caption('Connect 4') 

TEAL = (0, 128, 128) 
SILVER = (192, 192, 192) 
DARK_GREY = (70, 70, 70) 
BROWN = (174, 94, 0) 

screen.fill(TEAL) 
for rows in range(1, 7): 
    for columns in range(1, 8): 
        pygame.draw.circle(screen, SILVER, (columns * 2 * 30, 50 * rows), 20, 0) 

user1Token = DARK_GREY 
user2Token = BROWN 
dctofr_c = {} 

def user_turn(posofrow, posofcolumn, userToken): 
    pygame.draw.circle(screen, userToken, (posofcolumn * 2 * 30, 50 * posofrow), 20, 0) 
    dctofr_c[posofrow, posofcolumn] = turn 
    return 

def valid_row(row, column, userToken): 
    if row > 6: 
        print("BOARD IS FULL" "\n" "GAME OVER") 
    else: 
        if (row, column) in dctofr_c: 
            return valid_row(row - 1, column, userToken) 
        else: 
            user_turn(row, column, userToken) 
    return 

def whos_turn(turn, row, column, user1Token, user2Token): 
    return valid_row(row, column, user1Token) if turn % 2 == 1 else valid_row(row, column, user2Token) 

def who_won(t1, t2, t3, t4, end): 
    if t1 % 2 == 0 and t2 % 2 == 0 and t3 % 2 == 0 and t4 % 2 == 0: 
        end = 1 
        print("user1 won" "\n" "GAME OVER") 
    elif t1 % 2 == 1 and t2 % 2 == 1 and t3 % 2 == 1 and t4 % 2 == 1: 
        end= 1 
        print("user2 won" "\n" "GAME OVER") 
    return end 

def check_horizontal(end): 
    for r in range(3, 7): 
        for c  in range(1, 5): 
            if (r, c) in dctofr_c and (r, c + 1) in dctofr_c and (r, c + 2) in dctofr_c and (r, c + 3) in dctofr_c: 
                t1 = dctofr_c[r, c] 
                t2 = dctofr_c[r, c + 1] 
                t3 = dctofr_c[r, c + 2] 
                t4 = dctofr_c[r, c + 3] 
                end = who_won(t1, t2, t3, t4, end) 
    return end 


def check_vertical(end): 
    r = 7 
    while r > 1: 
        r -= 1 
        for c in range(1, 8): 
            if (r, c) in dctofr_c and (r - 1, c) in dctofr_c and (r - 2, c) in dctofr_c and (r - 3, c) in dctofr_c: 
                t1 = dctofr_c[r, c] 
                t2 = dctofr_c[r - 1, c] 
                t3 = dctofr_c[r - 2, c] 
                t4 = dctofr_c[r - 3, c] 
                end = who_won(t1, t2, t3, t4, end) 
    return end 

def check_rightdiagonal(end): 
    for r in range(1, 5): 
        for c in range(4, 8): 
           if (r, c) in dctofr_c and (r + 1, c - 1) in dctofr_c and (r + 2, c - 2) in dctofr_c and (r + 3, c - 3) in dctofr_c: 
                t1 = dctofr_c[r, c] 
                t2 = dctofr_c[r + 1, c - 1] 
                t3 = dctofr_c[r + 2, c - 2] 
                t4 = dctofr_c[r + 3, c - 3] 
                end = who_won(t1, t2, t3, t4, end) 
    return end 

def check_leftdiagonal(end): 
    for r in range(1, 4): 
        for c in range(1, 5): 
            if (r, c) in dctofr_c and (r + 1, c + 1) in dctofr_c and (r + 2, c + 2) in dctofr_c and (r + 3, c + 3) in dctofr_c: 
                t1 = dctofr_c[r, c] 
                t2 = dctofr_c[r + 1, c + 1] 
                t3 = dctofr_c[r + 2, c + 2] 
                t4 = dctofr_c[r + 3, c + 3] 
                end = who_won(t1, t2, t3, t4,end) 
    return end 

def check_win(end): 
    end= check_horizontal(end) 
    end = check_vertical(end) 
    end = check_rightdiagonal(end) 
    end = check_leftdiagonal(end) 
    return end 

end = 0 
display = True 
while display: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            display = False 
            pygame.quit() 
            sys.exit() 
    row = 6 
    turn = 0 
    pygame.display.update() 
    if end == 1: 
        pygame.quit() 
        sys.exit() 
    while end == 0: 
        print("enter column where you want to drop the token") 
        column = int(input()) 
        if column < 1 or column > 7: 
            print("Please enter a valid column") 
        else: 
            turn += 1 
            if turn > 7: 
                end = check_win(end) 
            whos_turn(turn, row, column, user1Token, user2Token) 
            pygame.display.update() 