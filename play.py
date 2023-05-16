# Set Board size
board_width = 22
board_height = 11

# Board positions based off size, no. of rows is determined by height and vice versa.
board = [(row, column) for row in range(board_height) for column in range(board_width)]

# Worm
worm = [(board_height//2,6),(board_height//2,5),(board_height//2,4)]
movement = {'up': (-1,0), 'left': (0,-1), 'down': (1,0), 'right': (0,1)}
auto_move = movement['right']
# Worm auto direction = right, so I call the key from above dict to get the value.

# Gold Nuggets
gold_position = (5,15)

# Print board function
def print_board():
    for position in board:
        # Printing snake position
        if position in worm:
            print('O', end = '')
        # if position of row is a value of 0 or (board_height -1), or position of column is 0 or (board_height -1) then print border '#'
        elif position[0] in (0, board_height - 1) or position[1] in (0, board_width - 1):
            # printing border, need end as default is \n
            print('#', end = '')
        # Checking if cell is equal to gold position
        elif position == gold_position:
            print('G', end = '')
        else:
            # printing board space
            print(' ', end = '')
        
        # Starting new line once you reach right column. 
        if position[1] == board_width -1:
            # Defaults new line.
            print('')

def worm_movement():
    # Worm head = first tuple in worm, so to move worm we are adding a new head = direciton + old head, then removing tail(last tuple).
    update_worm = worm[0][0] + auto_move[0], worm[0][1] + auto_move[1]
    # Inserting new head as first tuple in worm, meaning I have 4 tuples.
    worm.insert(0,update_worm)
    # You can see there are now 4 tuples with print(worm), so you need to pop last tuple in list.
    worm.pop(-1)
    # If you print(worm) there are 3 tuples.




print_board()
