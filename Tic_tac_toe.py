import numpy as np
winner = 'no one'
#Def
def winnerchecker(grid):
    counterx = 0
    countero = 0
    for j in range(2):
        for a in (range(3)):
            test = grid[a,:]
            for b in test:
                if b == 'x':
                    counterx += 1
                elif b == 'x':
                    countero += 1
            if counterx == 3:
                return "X Won The Game"
            elif countero == 3:
                return 'O Won The Game'
            if counterx + countero == 9:
                return "Its A Tie"
            counterx = 0
            countero = 0
        grid = grid.T
    for b in range(2):
        for a in range(3):
                if grid[a][a] == 'x':
                    counterx += 1
                if grid[a][a] == 'o':
                    countero += 1
        if counterx == 3:
            return 'X Won The Game'
        elif countero == 3:
            return 'O Won The Game'
        counterx = 0
        countero = 0
        grid = np.rot90(grid)
    return 'no one'  
#Variables
basegrid=[['0', '1','2'],
	     ['3','4','5'],
	     ['6','7','8']] 
grid = [['0', '1','2'],  
	    ['3','4','5'],   
	    ['6','7','8']]   
full = 'Someone'
counter = 0
#Game start
option = input('Do you want to New or Load: ')
if option == 'New':
    loadfile = input('What will be the Name of this file: ')
    f = open('{}.txt'.format(loadfile),'w')
    f.write('0')
    for a in range(3):
            f.write('\n')
            for c in range(3):
                f.write(basegrid[a][c])
    f.close()
if option == 'Load':
    loadfile = input('What was the name of the file: ')
while winner == 'no one':
        # Counter
    f = open(loadfile+'.txt','r')
    lines = f.readlines() 
    f.close()
    counter = lines.pop(0)
    counter = int(counter)
    grid = [] 
    for line in lines:
        line = line.strip()
        row = []
        for move in line:
            row.append(move)
        grid.append(row)       
    player = ['x','o','x','o','x','o','x','o','x']
    players = player[counter]
    playerss = players.upper()
    location = int(input('Player {} turn. Where would you like to place?  '.format(str(playerss))))
    print('')
    if location in range(10):
        row = location//3 
        col = location%3
        if grid[row][col] == 'x' or grid[row][col] == 'o':
            counter -= 1
            print('Pick another location')
        else:
            grid[row][col] = players
    else:
        print('Please pick a number on the board')
    counter += 1   
    # auto save
    f = open(loadfile+'.txt', 'w')
    f.write(str(counter))
    for a in range(3):
        f.write('\n')
        for c in range(3):
            f.write(grid[a][c])
    f.close()
    # Board
    for a in range(3):
        for b in range(3):
            if not b == 2:
                print(grid[a][b],end='|')
            else:
                print(grid[a][b])
        if not a == 2:
            print('-----')      
    print('\n')

    #checker
    grid = np.array(grid)
    winner = winnerchecker(grid)
        
    if winner == 'no one':
        print('Continue')
#-----------------------------------------------------------------------------
    elif winner != 'no one':
        print(winner)
        decision = input('Do you want to play another round? (yes/no) ')
        f = open('{}.txt'.format(loadfile), 'w')
        f.write('0')
        for a in range(3):
            f.write('\n')
            for c in range(3):
                f.write(basegrid[a][c])
        f.close()        
        if decision == 'yes':
            winner = 'no one'