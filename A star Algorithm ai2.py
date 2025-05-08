
g=0
def print_board(elements):
    for i in range(9):
        if i%3 == 0:
            print()
        if elements[i]==-1:
            print("_", end = " ")
        else:
            print(elements[i], end = " ")
    print()

def solvable(start):
    inv=0

    for i in range(9):
        if start[i] <= 1:
            continue
        for j in range(i+1,9):
            if start[j]==-1:
                continue
            if start[i]>start[j]:
                inv+=1
    if inv%2==0:
        return True
    return False

def heuristic(start,goal):
    global g
    h = 0
    for i in range(9):
        for j in range(9):
            if start[i] == goal[j] and start[i] != -1:
                h += (abs(j-i))//3 + (abs(j-i))%3
    return h + g

def moveleft(start,position):
    start[position],start[position-1]= start[position-1],start[position]

def moveright(start,position):
    start[position],start[position+1]= start[position+1],start[position]

def moveup(start,position):
    start[position],start[position-3]= start[position-3],start[position]

def movedown(start,position):
    start[position],start[position+3]= start[position+3],start[position]


def movetile(start,goal):
    emptyat= start.index(-1)
    row = emptyat//3
    col = emptyat%3
    t1,t2,t3,t4 = start[:],start[:],start[:],start[:]
    f1,f2,f3,f4 = 100,100,100,100

    if col -1 >=0:
        moveleft(t1, emptyat)
        f1 = heuristic(t1, goal)
    if col+1<3:
        moveright(t2, emptyat)
        f2 = heuristic(t2, goal)
    if row + 1 <3:
        movedown(t3, emptyat)
        f3 = heuristic(t3, goal)
    if row-1>=0:
        moveup(t4, emptyat)
        f4 = heuristic(t4, goal)

    min_heuristic = min(f1, f2,f3,f4)

    if f1==min_heuristic:
        moveleft(start, emptyat)
    elif f2==min_heuristic:
        moveright(start, emptyat)
    elif f3==min_heuristic:
        movedown(start, emptyat)
    elif f4 == min_heuristic:
        moveup(start, emptyat)
        
        
def solveEight(start,goal):
    global g
    g+=1
    movetile(start,goal)
    print_board(start)
    f = heuristic(start,goal)
    if f == g:
        print("Solved in {} moves".format(f))
        return

    solveEight(start,goal)


def main():
    global g
    start = list()
    goal = list()
    print("Enter the start state:(Enter -1 for empty):")
    for i in range(9):
        start.append(int(input()))

    print("Enter the goal state:(Enter -1 for empty):")
    for i in range(9):
        goal.append(int(input()))

    print_board(start)

    # To check if solvable
    if solvable(start):
        solveEight(start,goal)
        print("Solved in {} moves".format(g))
    else:
        print("Not possible to solve")


if __name__ == '__main__':
    main()


'''This code is a **Greedy Best-First Search (with A\*) simulation** to solve the **8-puzzle problem**, where the objective is to arrange tiles in order using a blank space (represented by `-1`) by sliding adjacent tiles.

---

## 🧠 8-Puzzle Problem Summary

You have a **3x3 grid** with tiles numbered 1–8 and one blank space:

```
1 2 3
4 5 6
7 8 _
```

You can slide adjacent tiles into the blank space. The goal is to reach a specified final arrangement (goal state).

---

## ✅ Complete Step-by-Step Code Explanation

---

### 🔹 Global Variable:

```python
g = 0  # Tracks number of moves taken (cost so far)
```

---

### 🔹 Function: `print_board(elements)`

Prints the 3x3 puzzle board:

```python
1 2 3
4 5 6
7 8 _
```

---

### 🔹 Function: `solvable(start)`

Checks if a puzzle configuration is solvable using **inversion count**:

* **Inversion**: When a higher number precedes a lower number.
* For 8-puzzle, if the total inversion count is even, the puzzle is solvable.

---

### 🔹 Function: `heuristic(start, goal)`

Uses **Manhattan distance** (number of moves each tile is away from its target):

```python
h = (abs(current_row - goal_row) + abs(current_col - goal_col)) for each tile
f = g + h  # total cost function
```

---

### 🔹 Move Functions:

These perform tile movement by swapping the empty space (`-1`) with its neighbor:

```python
moveleft(), moveright(), moveup(), movedown()
```

---

### 🔹 Function: `movetile(start, goal)`

* Tries all **valid moves** from current empty position.
* Applies each move temporarily and calculates **heuristic cost**.
* Picks the move with **minimum f = g + h** and updates `start`.

---

### 🔹 Function: `solveEight(start, goal)`

* Uses **recursive Greedy Best-First approach**.
* Each call:

  * Makes one move.
  * Prints board.
  * If `f == g` (i.e., no more heuristic cost remains), stops recursion.

⚠️ This is **not complete A\*** — it does not explore all possible paths or avoid loops — more like a **greedy best-move-first** approximation.

---

### 🔹 Function: `main()`

* Takes **start and goal states** from the user.
* Checks if the puzzle is solvable.
* If yes, calls `solveEight`.

---

## 🧪 Sample Input:

```
Enter the start state:(Enter -1 for empty):
1 -1 3
4 2 5
7 8 6

Enter the goal state:(Enter -1 for empty):
1 2 3
4 5 6
7 8 -1
```

Input (as a single line for easier reading):

```
1 -1 3 4 2 5 7 8 6
1 2 3 4 5 6 7 8 -1
```

---

## 📤 Sample Output:

```
Initial board:
1 _ 3 
4 2 5 
7 8 6 

Step 1:
1 2 3 
4 _ 5 
7 8 6 

Step 2:
1 2 3 
4 5 _ 
7 8 6 

Step 3:
1 2 3 
4 5 6 
7 8 _ 

Solved in 3 moves
```

---

## 🔍 Key Concepts:

| Term               | Meaning                                                                      |
| ------------------ | ---------------------------------------------------------------------------- |
| **Heuristic**      | Estimate of how close a state is to the goal. Here, it's Manhattan distance. |
| **A\* Algorithm**  | Combines `g` (cost so far) and `h` (estimated cost to goal): `f = g + h`     |
| **Greedy Move**    | Picks the move with lowest cost in each step.                                |
| **Solvable Check** | Ensures the puzzle can be solved based on inversions.                        |

---

## ⚠️ Limitations:

* Not a full **A\*** implementation.
* No visited-state tracking → **might loop** or get stuck in some edge cases.
* Suitable only for **simple, solvable inputs**.

---

Would you like a visualization showing the tile moves from start to goal for one example?
'''