directory="C:/Users/engri/Downloads/sudoku puzzle.txt"      #change this to your directory of the sudoku puzzle.txt file, make sure to replace the \ with /





import time
steps = 0
backtracks = 0




def inRow(puzzle,row,val):       #checking if the value is already in this row or not
    if val in puzzle[row]:
        return True
    else:
        return False
    
def inCol(puzzle,row,col,val):   #checking if the value is already in this column or not
    for i in range(9):
        if puzzle[i][col]==val:
            return True
    return False
        
def inSubgrid(puzzle,row,col,val):                    #checking if the value is already in this subgrid or not
    for i in range(int(row/3)*3,(int(row/3)*3)+3):
        for j in range(int(col/3)*3,(int(col/3)*3)+3):
            if puzzle[i][j]==val:
                return True
    return False

def checkValid(puzzle, row, col, val):                 #combining the other checks
    if inRow(puzzle, row, val)==False and inCol(puzzle, row, col, val)==False and inSubgrid(puzzle, row, col, val)==False:
        return True
    else:
        return False
    
    
    
    


def initialValid(puzzle):             #NEED TO FIX
    for row in range(9):
        for col in range(9):
            val=puzzle[row][col]
            if val!=0:
                puzzle[row][col]=0  #we are setting it to 0 cuz without this it invalidates itself for some reason 
                if not checkValid(puzzle, row, col, val):  #just using the check function again here
                    puzzle[row][col]=val  # restore
                    return False
                puzzle[row][col]=val  
    return True
   

    
    
    
    
                                         
def createDomain(puzzle):          #basically creating a domain of possible allowed values for each cell
    domains = {}
    for row in range(9):
        for col in range(9):
            if puzzle[row][col]==0:
                possibleValues=set()
                for n in range(1,10):
                    if checkValid(puzzle, row, col, n)==True:
                        possibleValues.add(n)
                domains[(row,col)]=possibleValues    
            else:
                domains[(row,col)]={puzzle[row][col]}       #for self, this is basically jst saying if theres already a 
    return domains                                          #value in that cell then that value is the only one in its domain







def MRVHeuristic(domains, puzzle):   #basically its picking out the empty cell with the smallest domain to be filled first
    unassigned=[]
    for row in range(9):
        for col in range(9):
            if puzzle[row][col]==0:
                unassigned.append((row,col))
    if not unassigned:
        return None
    def domainSize(cell):
        return len(domains[cell])
    smallestCell=min(unassigned,key=domainSize)
    return smallestCell






def forwardCheck(puzzle,domains,row,col,val):
    updatedDomains={}
    for coordinates,values in domains.items():
        updatedDomains[coordinates]=set(values)        #for self, we r basically just making a copy of domains
    puzzle[row][col]=val
    updatedDomains[(row,col)]={val}   #we are making the domain of a cell one value, and
    for i in range(9):                #then seeing how that affects the domains of the other cells in that row, column, and subgrid
        for j in range(9):
            if (i==row or j==col or (int(i/3))==int(row/3) and int(j/3)==int(col/3)) and (i,j)!=(row,col):
                if val in updatedDomains[(i,j)]:
                    updatedDomains[(i, j)]=updatedDomains[(i,j)]-{val}
                    if len(updatedDomains[(i,j)])==0:
                        puzzle[row][col]=0 #we r just changing the temporary value back  to zero now
                        return None
    return updatedDomains





def backtrack(puzzle, domains):
    global steps
    global backtracks
    steps =steps+1
    MRVcell = MRVHeuristic(domains,puzzle)
    if MRVcell is None:       
        return True         #if there r no more MRVcells then the sudoku is solved
    for val in sorted(domains[MRVcell]):
        updatedDomains = forwardCheck(puzzle,domains,MRVcell[0],MRVcell[1],val)    #doing 
        if updatedDomains!=None:
            if backtrack(puzzle,updatedDomains)==True:
                return True
        puzzle[MRVcell[0]][MRVcell[1]]=0     #resetting the value back to 0 again
        backtracks=backtracks+1
    return False










def solvePuzzle(puzzle):
    global steps
    global backtracks
    steps=0
    backtracks=0
    timerStart=time.time()
    if not initialValid(puzzle):
        print("Invalid initial puzzle.")
        timeTaken=0
        return False,steps,backtracks,timeTaken
    domains=createDomain(puzzle)
    solving=backtrack(puzzle,domains)
    timerStop=time.time()
    timeTaken=timerStop-timerStart
    return solving,steps,backtracks,timeTaken




def readFile(filename):
    grid=[]
    with open(filename,"r") as file:
        for line in file:
            line=line.strip()
            lineInt=[int(l) for l in line]
            grid.append(lineInt)
    return grid




grid=readFile(directory)
solving,steps,backtracks,timeTaken=solvePuzzle(grid)
if solving==True:
    print("Solved sudoku puzzle:")
    for row in grid:
        print(row)
else:
    print("No solution found.")
print(f"Steps: {steps}")
print(f"Backtracks: {backtracks}")




import tkinter



def GUI(puzzle):
    root = tkinter.Tk()
    root.title("Sudoku Puzzle Solver")
    entries=[]
    for x in range(9):
        row=[]
        for y in range(9):
            row.append(None)    #creating a row with empty cells
        entries.append(row)       #creating the whole 9x9 with empty cells by combining the rows
    for i in range(9):
        for j in range(9):
            cellBox= tkinter.Entry(root,width=2,font=('Times New Roman',16),justify='center')
            cellBox.grid(row=i,column=j)
            if puzzle[i][j]!=0:
                cellBox.insert(0,str(puzzle[i][j]))    
            entries[i][j]=cellBox      #basically we are just inserting the initial values into that empty 9x9 we had

    answerLabel=tkinter.Label(root,text="",font=('Times New Roman', 12)) #this is to create the area where the result of the solving and the steps and stuff show up
    answerLabel.grid(row=10, column=0, columnspan=9)       #columnspan 9 works best and dosent mess up the arrangement of the matrix, im pretty sure cuz there are 9 columns in the puzzle itself

    def whenSolve():              #this is for when we click the solve button
        grid=[]
        for i in range(9):
            row=[]
            for j in range(9):
                vals=entries[i][j].get()
                if vals == "":
                    row.append(0)  # empty cell
                elif vals.isdigit() and 0<=int(vals)<=9:  # only allow 0-9
                    row.append(int(vals))
                else:
                    answerLabel.config(text="Invalid or unsolvable puzzle.")
                    return
            grid.append(row)
        solving,steps,backtracks,timeTaken=solvePuzzle(grid)
        if solving:
            for i in range(9):
                for j in range(9):
                    entries[i][j].delete(0,tkinter.END)
                    entries[i][j].insert(0,str(grid[i][j]))
                    entries[i][j].config(state='disabled')
            answerLabel.config(text=
                               f'''Solved! Steps: {steps},
Backtracks: {backtracks}
Time: {timeTaken:.3f} seconds''')
        else:
            answerLabel.config(text="Invalid or unsolvable puzzle.")

    tkinter.Button(root,text="Solve",font=('Times New Roman',14),command=whenSolve).grid(row=9,columnspan=9,pady=5)
    root.mainloop()

grid=readFile(directory)
GUI(grid)
