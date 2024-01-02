Sudoku = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def Solve(Sudoku):
  coord = EmptyCoord(Sudoku)
  if not coord:
    return True # if no empty coords remain it exits the whole recursion
  y, x = coord
  for checker in range(1, 10):
    if Valid(Sudoku, y, x, checker):
      Sudoku[y][x] = checker
      if Solve(Sudoku): # checks if next one can be true if not make the current one 0 to skip the checker by 1 
        return True 
      else:
       Sudoku[y][x] = 0 
  return False

def EmptyCoord(Sudoku):
  for outerlooper in range(9):
    for innerlooper in range(9):
      if Sudoku[outerlooper][innerlooper] == 0:
        return outerlooper, innerlooper # [y,x]
  return None

def Valid(Sudoku, y, x, checker): #check row column and 3x3
  counter = 0
  for looper in range(9):
    if Sudoku[y][looper] != checker:
      counter += 1
  if counter >= 9:
    for looper in range(9):
      if Sudoku[looper][x] != checker:
        counter += 1
  if counter >= 18 :
    for looper in range(9):
      if Sudoku[3 * (y // 3) + looper // 3][3 * (x // 3) + looper % 3] != checker:
        counter += 1
  if counter >= 27 :
    return True
  else:
    return False


      

if Solve(Sudoku):
  for row in Sudoku:
    print(row)
else:
  print("Unsolvable")
