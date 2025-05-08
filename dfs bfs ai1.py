def dfs(visited,graph,node):
    if node not in visited:
        print(node,end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited,graph,node,queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s,end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    visited1 = set() # TO keep track of DFS visited nodes
    visited2 = set() # TO keep track of BFS visited nodes
    queue = []       # For BFS
    n = int(input("Enter number of nodes : "))
    graph = dict()

    for i in range(1,n+1):
        edges = int(input("Enter number of edges for node {} : ".format(i)))
        graph[i] = list()
        for j in range(1,edges+1):
            node = int(input("Enter edge {} for node {} : ".format(j,i)))
            graph[i].append(node)

    print("The following is DFS")
    dfs(visited1, graph, 1)
    print()
    print("The following is BFS")
    bfs(visited2, graph, 1, queue)

if __name__=="__main__":
    main()

















'''Let's go through the **complete explanation** of the provided **DFS and BFS code**, along with its **expected output** and **explanation of all relevant terms**.

---

## ✅ **What Does the Code Do?**

This Python program performs **Depth First Search (DFS)** and **Breadth First Search (BFS)** traversal on a **user-defined graph** (represented using an adjacency list in a dictionary). The traversal starts from **node 1**.

---

## 💡 **Key Concepts Explained**

### 🔸 Graph

A **graph** is a non-linear data structure consisting of **nodes (vertices)** and **edges** (connections between nodes).

Example:

```
1 -- 2
|    |
3 -- 4
```

### 🔸 Adjacency List

A way to represent a graph where each node points to a list of its neighbors.

```python
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3]
}
```

---

## 🔹 DFS (Depth First Search)

### ✅ How it works:

* Goes **deep into each branch** before backtracking.
* Implemented using **recursion**.
* Uses a **set `visited`** to keep track of already visited nodes.

### 📘 Code Explanation:

```python
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
```

---

## 🔹 BFS (Breadth First Search)

### ✅ How it works:

* Visits **all neighbors** of a node before going to next level.
* Implemented using a **queue**.
* Also uses a **set `visited`**.

### 📘 Code Explanation:

```python
def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
```

---

## 🔸 `main()` Function

Handles:

* Taking user input for number of nodes and their edges.
* Constructing the graph.
* Calling DFS and BFS.

---

## ✅ Sample Input and Output

### Suppose this is your input:

```
Enter number of nodes : 4
Enter number of edges for node 1 : 2
Enter edge 1 for node 1 : 2
Enter edge 2 for node 1 : 3
Enter number of edges for node 2 : 1
Enter edge 1 for node 2 : 4
Enter number of edges for node 3 : 1
Enter edge 1 for node 3 : 4
Enter number of edges for node 4 : 0
```

### Then the graph looks like:

```python
graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}
```

### Output:

```
The following is DFS
1 2 4 3 
The following is BFS
1 2 3 4 
```

---

## 🔎 DFS Traversal Explanation:

Starting at **1**:

* Visit **1**
* Go to **2**
* From **2**, go to **4**
* 4 has no children, so backtrack
* From 1, now go to **3** (even though it also connects to 4, it's already visited)

Order: **1 → 2 → 4 → 3**

---

## 🔎 BFS Traversal Explanation:

Start at **1**:

* Visit 1 → Queue: `[2, 3]`
* Visit 2 → Queue: `[3, 4]`
* Visit 3 → (4 already in queue) → Queue: `[4]`
* Visit 4 → Queue: `[]`

Order: **1 → 2 → 3 → 4**

---

## 📘 Summary of Important Terms:

| Term               | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| **Graph**          | A collection of nodes and edges.                              |
| **Node/Vertex**    | A single point in the graph.                                  |
| **Edge**           | A connection between two nodes.                               |
| **Adjacency List** | A dictionary storing node neighbors.                          |
| **DFS**            | Recursively explores as deep as possible before backtracking. |
| **BFS**            | Explores all neighbors level by level using a queue.          |
| **Visited Set**    | Keeps track of already visited nodes to avoid cycles.         |
| **Queue**          | FIFO structure used in BFS.                                   |

---

Would you like a diagram of how the graph looks or a dry-run visualization of both algorithms step-by-step?

'''