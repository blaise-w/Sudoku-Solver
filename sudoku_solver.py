import setup

#helpful, but not needed
class variables:
	counter=0

def sudoku_backtracking(sudoku):
	variables.counter = 0
	#put your code here
	frontier = []
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				frontier.append((i, j))
	check(sudoku, frontier)
	return variables.counter

def check(sudoku, frontier):
	variables.counter += 1
	if len(frontier) == 0: return True
	current = frontier.pop(0)
	y = current[0]
	x = current[1]
	for i in range(1, 10):
		if (setup.can_yx_be_z(sudoku, y, x, i)):
			sudoku[y][x] = i
			if check(sudoku, frontier[:]): return True
			sudoku[y][x] = 0
	return False

			


def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	#put your code here
	frontier = []
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				frontier.append((i, j))
	check_f(sudoku, frontier)
	return variables.counter

def check_f(sudoku, frontier):
	variables.counter += 1
	if len(frontier) == 0: return True
	current = frontier.pop(0)
	y = current[0]
	x = current[1]
	for i in range(1, 10):
		if (setup.can_yx_be_z(sudoku, y, x, i)):
			sudoku[y][x] = i

			if forward_check(sudoku, frontier):
				sudoku[y][x] = 0
				continue

			if check_f(sudoku, frontier[:]): return True
			sudoku[y][x] = 0
	return False

def forward_check(sudoku, frontier):
	for i in frontier:
		y = i[0]
		x = i[1]
		c = 0
		for j in range(1, 10):
			if (setup.can_yx_be_z(sudoku, y, x, j)): c += 1
		if c == 0: return True
	return False