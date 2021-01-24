# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:35:10 2021

@author: rxche
"""

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

# Solve board

def solve(board):
    
    #Base case of recursion 
    find=find_empty(board)
    if not find:
        return True 
    else: 
        row, col = find
    # Recursive step
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            
            #Until all squares are filled
            if solve(board):
                return True
            #Backtrack and reset to 0
            board[row][col] = 0 
            
    return False
# Print out board

def print_board(board):
    
    for i in range(len(board)):
        if i % 3 ==0 and i != 0:
            print("- - - - - - - - - - - - - ")
            
        for j in range(len(board)):
            if j % 3 ==0 and j!= 0: 
                print("| ", end="")
                    
            if j == 8: 
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Find empty square

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0: 
                return (i, j) # returns (row, col), (y,x)
    return None

# Check if digit is already in row, column, or box

def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        
    
    # Check column 
    
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False 
        
    # Check box
    box_x= pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y *3 +3 ):
        for j in range(box_x * 3, box_x *3 + 3) :
            if board[i][j] == num and (i,j) != pos: 
                return False 
            
    return True 

print_board(board)
solve(board)
print("Finished solution")
print_board(board)

