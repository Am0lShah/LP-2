import sys

V = 5

def minKey(key, mstSet):
    min_val = sys.maxsize
    min_index = -1
    for v in range(V):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index

def printMST(parent, graph):
    print("Edge \tWeight")
    for i in range(1, V):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")

def primMST(graph):
    key = [sys.maxsize] * V
    parent = [None] * V
    mstSet = [False] * V

    key[0] = 0
    parent[0] = -1

    for _ in range(V - 1):
        u = minKey(key, mstSet)
        mstSet[u] = True

        for v in range(V):
            if graph[u][v] > 0 and not mstSet[v] and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    printMST(parent, graph)

if __name__ == "__main__":
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    primMST(graph)
















'''This Python code is a classic implementation of **Prim’s Algorithm** for finding the **Minimum Spanning Tree (MST)** of a weighted, undirected graph using an **adjacency matrix**.

Let’s break it down for clarity and better understanding:

---

## 🧠 **What is Prim's Algorithm?**

Prim’s algorithm is a **greedy algorithm** that builds the MST one node at a time by:

* Picking the **smallest edge** that connects a node **inside the MST** to a node **outside** of it.

---

## 📑 **Code Explanation**

### 🔢 Constants

```python
V = 5
```

* Number of vertices in the graph.

---

### 🔍 `minKey(key, mstSet)`

Finds the index (vertex) with the **minimum key value** not yet included in MST.

```python
min_val = sys.maxsize  # Initially set to infinity
```

* `key[]`: Minimum weight edge to add a vertex.
* `mstSet[]`: Boolean list indicating if a vertex is included in MST.

---

### 🖨️ `printMST(parent, graph)`

Prints the constructed MST.

```python
for i in range(1, V):
    print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")
```

* `parent[]`: Stores the parent node for each vertex in the MST.

---

### 🌳 `primMST(graph)`

Main logic for building the MST.

```python
key = [sys.maxsize] * V       # Initially all keys are infinite
parent = [None] * V           # Stores MST structure
mstSet = [False] * V          # Keeps track of included vertices

key[0] = 0                    # Start from vertex 0
parent[0] = -1                # No parent for starting vertex
```

#### MST Construction Loop

```python
for _ in range(V - 1):  # MST has V-1 edges
    u = minKey(key, mstSet)  # Pick the minimum key vertex
    mstSet[u] = True         # Mark it as included

    # Update key and parent for adjacent vertices
    for v in range(V):
        if graph[u][v] > 0 and not mstSet[v] and  > graph[u][v]:
            key[v] = graph[u][v]
            parent[v] = u
```

---

## 🧪 **Sample Input Graph**

```python
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, ],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
```

This graph can be visualized like this:

```
     2       3       7
(0)---(1)---(2)     /
 |     |     |     /
 6     8     |    5
 |     |     |   /
(3)---(4)---(4)
     9
```

---

### ✅ **Expected Output**

```plaintext
Edge    Weight
0 - 1    2
1 - 2    3
0 - 3    6
1 - 4    5
```

This shows the **Minimum Spanning Tree** and the edges selected with their weights.

---

## ✅ Concepts Covered

| Concept          | Explanation                                                                      |
| ---------------- | -------------------------------------------------------------------------------- |
| Greedy Algorithm | Always picks the least weight edge                                               |
| Graphs           | Represented as adjacency matrix                                                  |
| MST              | A subset of edges that connects all vertices with no cycles and min total weight |

---

## 🚀 Suggestions for Improvement

1. **Dynamic vertex input** instead of hardcoded `V = 5`.
2. **Graph input from user or file** for flexibility.
3. **Graph visualization** using libraries like `networkx` and `matplotlib`.

---

Would you like me to convert this into a **graph visualizer** using `networkx` so you can **see the MST diagrammatically**?
'''



'''import matplotlib.pyplot as plt
import networkx as nx

# Define the graph as in the Prim's example
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

V = len(graph)

def primMST(graph):
    import sys
    key = [sys.maxsize] * V
    parent = [None] * V
    mstSet = [False] * V

    key[0] = 0
    parent[0] = -1

    for _ in range(V - 1):
        min_val = sys.maxsize
        u = -1
        for v in range(V):
            if not mstSet[v] and key[v] < min_val:
                min_val = key[v]
                u = v
        mstSet[u] = True

        for v in range(V):
            if graph[u][v] > 0 and not mstSet[v] and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    return parent

# Generate the MST
parent = primMST(graph)

# Create a graph using networkx
G = nx.Graph()

# Add all edges from the original graph for full visualization
for i in range(V):
    for j in range(i + 1, V):
        if graph[i][j] != 0:
            G.add_edge(i, j, weight=graph[i][j])

# Create a list of MST edges
mst_edges = [(parent[i], i) for i in range(1, V)]

# Set layout
pos = nx.spring_layout(G, seed=42)

# Draw full graph edges in gray
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1, edge_color='gray')

# Draw MST edges in red and thicker
nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=2.5, edge_color='red')

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')

# Draw labels
nx.draw_networkx_labels(G, pos)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Minimum Spanning Tree using Prim's Algorithm (MST in Red)")
plt.axis('off')
plt.tight_layout()
plt.show()
'''















'''

// Here's a **complete explanation of the given C++ code**, which implements **Prim’s Algorithm** to find the **Minimum Spanning Tree (MST)** of a graph, along with the **output** for the provided `graph`.

// ---

// ## 🔧 **Concepts Used:**

// ### ✅ Graph

// * A set of vertices (nodes) connected by edges.
// * Represented as a 2D array (adjacency matrix) in this code.

// ### ✅ MST (Minimum Spanning Tree)

// * A subset of the edges that connects all vertices together without any cycles and with the **minimum possible total edge weight**.

// ### ✅ Prim's Algorithm

// * A greedy algorithm that builds the MST by picking the **cheapest edge** that connects a new vertex to the growing tree.

// ---

// ## 🧠 **Explanation of Code Components**

// ### 🔹 `#define V 5`

// Defines the number of vertices in the graph.

// ### 🔹 `minKey(int key[], bool mstSet[])`

// Finds the vertex not yet included in MST with the **minimum key value**.

// * `key[]`: holds the minimum weight edge to each vertex.
// * `mstSet[]`: tracks which vertices are already included in the MST.

// ### 🔹 `printMST(int parent[], int graph[V][V])`

// Prints the MST by using the `parent[]` array where:

// * `parent[i]` stores the parent of vertex `i` in the MST.

// ### 🔹 `primMST(int graph[V][V])`

// Core of Prim's Algorithm:

// * Initializes all keys to `INT_MAX` (infinity).
// * Starts with vertex 0 by setting `key[0] = 0`.
// * In each iteration:

//   * Picks the minimum key vertex not in the MST.
//   * Updates the key and parent of its adjacent vertices if a cheaper edge is found.

// ### 🔹 `main()`

// Defines the graph and calls `primMST()` to compute and print the MST.

// ---

// ## 🟩 **Input Graph** (Adjacency Matrix):

// ```
//      0   1   2   3   4
//   -----------------------
// 0 |  0   2   0   6   0
// 1 |  2   0   3   8   5
// 2 |  0   3   0   0   7
// 3 |  6   8   0   0   9
// 4 |  0   5   7   9   0
// ```

// ---

// ## 📤 **Output**

// ```
// Edge    Weight
// 0 - 1   2
// 1 - 2   3
// 0 - 3   6
// 1 - 4   5
// ```

// ### ✅ **Explanation:**

// * Edge 0–1 has weight 2 → Added
// * Edge 1–2 has weight 3 → Added
// * Edge 0–3 has weight 6 → Added
// * Edge 1–4 has weight 5 → Added

// 🔸 These edges connect all nodes with no cycles, and the total weight = **2 + 3 + 6 + 5 = 16** (minimum possible).

// ---

// ## 🧾 Summary of Key Terms:

// | Term                 | Meaning                                                |
// | -------------------- | ------------------------------------------------------ |
// | **MST**              | Tree covering all nodes with minimum total edge weight |
// | **Greedy Algorithm** | Always picks the lowest-cost choice at each step       |
// | **Key Array**        | Stores the minimum weight edge to each vertex          |
// | **Parent Array**     | Stores the MST structure                               |
// | **Adjacency Matrix** | Matrix representing edge weights between nodes         |

// ---

// Would you like a step-by-step visualization image of how Prim’s Algorithm builds the MST on this graph?


















// [![Virtual Labs](https://images.openai.com/thumbnails/94df2913a74870d671abac330cd5e577.png)](https://ds2-iiith.vlabs.ac.in/exp/min-spanning-trees/prims-algorithm/demo-of-prims-algorithm.html)

// Certainly! Let's walk through a step-by-step visualization of **Prim's Algorithm** applied to the provided graph.

// ---

// ### 🗺️ **Graph Overview**

// The graph is represented as an adjacency matrix:

// ```
//      0   1   2   3   4
//    ---------------------
// 0 |  0   2   0   6   0
// 1 |  2   0   3   8   5
// 2 |  0   3   0   0   7
// 3 |  6   8   0   0   9
// 4 |  0   5   7   9   0
// ```

// This corresponds to the following undirected, weighted graph:

// * Edge 0–1: Weight 2
// * Edge 0–3: Weight 6
// * Edge 1–2: Weight 3
// * Edge 1–3: Weight 8
// * Edge 1–4: Weight 5
// * Edge 2–4: Weight 7
// * Edge 3–4: Weight 9

// ---

// ### 🔍 **Step-by-Step Execution of Prim's Algorithm**

// **Initialization:**

// * Start with vertex **0**.
// * MST Set: `{0}`
// * Edges considered:

//   * Edge 0–1 (Weight 2)
//   * Edge 0–3 (Weight 6)

// **Step 1:**

// * Select the edge with the minimum weight connecting to MST: **Edge 0–1 (Weight 2)**.
// * Add vertex **1** to MST Set: `{0, 1}`
// * Edges considered:

//   * Edge 1–2 (Weight 3)
//   * Edge 1–3 (Weight 8)
//   * Edge 1–4 (Weight 5)
//   * Edge 0–3 (Weight 6)

// **Step 2:**

// * Select the edge with the minimum weight connecting to MST: **Edge 1–2 (Weight 3)**.
// * Add vertex **2** to MST Set: `{0, 1, 2}`
// * Edges considered:

//   * Edge 2–4 (Weight 7)
//   * Edge 1–3 (Weight 8)
//   * Edge 1–4 (Weight 5)
//   * Edge 0–3 (Weight 6)([College of Arts and Sciences][1], [GeeksforGeeks][2])

// **Step 3:**

// * Select the edge with the minimum weight connecting to MST: **Edge 1–4 (Weight 5)**.
// * Add vertex **4** to MST Set: `{0, 1, 2, 4}`
// * Edges considered:

//   * Edge 4–3 (Weight 9)
//   * Edge 0–3 (Weight 6)
//   * Edge 1–3 (Weight 8)

// **Step 4:**

// * Select the edge with the minimum weight connecting to MST: **Edge 0–3 (Weight 6)**.
// * Add vertex **3** to MST Set: `{0, 1, 2, 3, 4}`
// * All vertices are now included in the MST.

// ---

// ### 🌳 **Final MST Edges and Total Weight**

// * Edge 0–1: Weight 2
// * Edge 1–2: Weight 3
// * Edge 1–4: Weight 5
// * Edge 0–3: Weight 6

// **Total Weight:** 2 + 3 + 5 + 6 = **16**

// ---

// ### 📊 **Visual Representation**

// For a visual step-by-step demonstration of Prim's Algorithm, you can explore the following resources:

// * **GeeksforGeeks:** Provides a detailed explanation with diagrams. ([GeeksforGeeks][2])

// * **VisuAlgo:** Offers interactive visualizations of Prim's Algorithm. ([VisuAlgo][3])

// * **USFCA Visualization:** An interactive tool to visualize Prim's Algorithm on various graphs. ([College of Arts and Sciences][1])

// * **YouTube Tutorial:** A concise video explaining Prim's Algorithm with examples. ([YouTube][4])

// Feel free to explore these resources for a more in-depth understanding and visualization of Prim's Algorithm in action.

// ---

// [1]: https://www.cs.usfca.edu/~galles/visualization/Prim.html?utm_source=chatgpt.com "Prim MST Visualzation"
// [2]: https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/?utm_source=chatgpt.com "Prim's Algorithm for Minimum Spanning Tree (MST) | GeeksforGeeks"
// [3]: https://visualgo.net/en/mst?utm_source=chatgpt.com "Minimum Spanning Tree (Prim&#39 - VisuAlgo"
// [4]: https://www.youtube.com/watch?v=oDnlIP5pe5o&utm_source=chatgpt.com "Prim's Algorithm visualized | Graph Algorithm 2 - YouTube"
'''