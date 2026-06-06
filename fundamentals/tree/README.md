# Tree

A tree is a **non-linear** data structure made of nodes connected in a
**hierarchical** way.

Unlike an array, which stores elements in a linear sequence, a tree is used to
represent data with **parent-child relationships**.

---

## Why Trees Matter

Arrays are good for representing **order**.
Trees are good for representing **hierarchy**.

Examples of hierarchical data:

- File systems
- Company org charts
- Family trees
- HTML / DOM structure

Trees are also important because many advanced data structures belong to the
tree family, such as binary search trees, heaps, tries, and B-trees.

---

## Basic Terms

Consider this tree:

```text
        A
       / \
      B   C
     / \
    D   E
```

- **Node**: each element in the tree, such as `A`, `B`, or `C`
- **Root**: the top node of the tree, here `A`
- **Parent**: a node directly above another node
- **Child**: a node directly below another node
- **Leaf**: a node with no children, here `C`, `D`, and `E`
- **Edge**: a connection between two nodes
- **Subtree**: a node together with all nodes below it

Two important measurements:

- **Depth**: how far a node is from the root
- **Height**: how far a node can go down to its deepest leaf

In the example above:

- `B` has depth `1`
- `B` has height `1`

---

## Binary Tree

A binary tree is a special kind of tree where each node can have at most
**two children**.

These two positions are usually called:

- `left`
- `right`

Example:

```text
        A
       / \
      B   C
     /
    D
```

Binary trees are especially common because they are simple to model and are a
natural fit for recursive thinking.

---

## Common Shapes of Binary Trees

### Balanced

A balanced tree has left and right sides that are relatively even in height.

```text
        A
       / \
      B   C
     / \   \
    D   E   F
```

Balanced trees are generally more efficient than highly uneven trees.

### Skewed

A skewed tree grows mostly in one direction and starts to resemble a linked
list.

```text
    A
   /
  B
 /
C
/
D
```

Skewed trees are usually less efficient because their height becomes large.

### Full Binary Tree

In a full binary tree, every node has either:

- `0` children, or
- `2` children

No node has exactly one child.

### Complete Binary Tree

In a complete binary tree:

- every level is filled except possibly the last
- nodes in the last level are placed as far left as possible

This shape becomes especially important later when studying heaps.

---

## Basic Operations

Tree operations are different from array operations.

In an array, we often think about:

- index
- position
- left-to-right scanning

In a tree, we usually think about:

- the current node
- its `left` child
- its `right` child
- how to process its subtrees

Common ideas in tree operations:

- Represent a node with a value and references to child nodes
- Check whether a node is empty (`None`)
- Search by exploring the structure of the tree
- Insert or delete according to the rules of the specific tree type
- Traverse the whole tree in some order

An important difference:

- Arrays are mainly about **position**
- Trees are mainly about **relationships**

---

## Recursive Thinking on Trees

Tree problems are often solved with recursion because:

- a whole tree is a tree
- each subtree is also a tree

When solving a tree problem, a useful pattern is:

```text
solve(node):
    1. Handle the empty node
    2. Process the current node
    3. Solve the left subtree
    4. Solve the right subtree
    5. Combine the results
```

The most common base case is:

```text
node is None
```

For example, if we want to count the number of nodes:

```text
count(node) = 1 + count(node.left) + count(node.right)
```

And the base case is:

```text
count(None) = 0
```

This means:

- an empty node contributes `0`
- a non-empty node contributes `1`
- the final answer comes from combining the left and right subtree results

A good way to think about recursion is:

- the function solves the problem for the subtree rooted at `node`
- the current level trusts the recursive calls to solve the left and right subtrees correctly

---

## Tree Traversal

Traversal means visiting every node in a tree in some order.

Unlike arrays, trees do not have only one natural traversal order because a tree
branches into subtrees.

### DFS

Depth-first search (DFS) explores one branch deeply before backtracking.

For a binary tree, the three common DFS orders are:

- **Preorder**: `current -> left -> right`
- **Inorder**: `left -> current -> right`
- **Postorder**: `left -> right -> current`

Using this tree:

```text
        A
       / \
      B   C
     / \
    D   E
```

The traversal orders are:

- **Preorder**: `A B D E C`
- **Inorder**: `D B E A C`
- **Postorder**: `D E B C A`

These three traversals visit the same nodes, but the position of the
**current node** is different.

### BFS

Breadth-first search (BFS) visits nodes level by level.

For the same tree:

- **BFS / Level-order**: `A B C D E`

### DFS vs BFS

- **DFS**: go deep first, then backtrack
- **BFS**: visit one level at a time

---

## Why DFS Uses Recursion / Stack and BFS Uses Queue

The implementation style follows the traversal behavior.

### DFS and Stack

DFS tries to go as deep as possible before returning.

This matches **stack** behavior:

- the most recently discovered task is handled first
- this is **LIFO**: last in, first out

Recursion is a natural fit for DFS because recursive calls are managed by the
call stack.

So, conceptually:

- **DFS** = go deep first
- **Stack / Recursion** = natural tool for that behavior

### BFS and Queue

BFS visits nodes level by level.

This matches **queue** behavior:

- nodes discovered earlier are processed earlier
- this is **FIFO**: first in, first out

So, conceptually:

- **BFS** = process one level at a time
- **Queue** = natural tool for that behavior

### Intuition

- **DFS** is like walking down one path in a maze until you must return
- **BFS** is like a wave expanding level by level

---

## When to Use Preorder, Inorder, and Postorder

The three DFS traversals differ only in where the **current node** is processed,
but that difference affects what each order is useful for.

### Preorder

Order:

```text
current -> left -> right
```

Use preorder when you want to:

- process the current node immediately
- pass information from parent to children
- think in a top-down way

Short intuition:

- **Preorder** = first process the current node, then go down

### Inorder

Order:

```text
left -> current -> right
```

This traversal is especially important in a **binary search tree (BST)**.

In a BST:

- values in the left subtree are smaller
- values in the right subtree are larger

So inorder traversal visits values in **sorted order**.

Short intuition:

- **Inorder** = left side, then current node, then right side
- in a BST, this gives an ordered result

### Postorder

Order:

```text
left -> right -> current
```

Use postorder when the current node depends on results from its children.

This is common in problems such as:

- computing height
- checking balance
- combining subtree results

Short intuition:

- **Postorder** = let the children finish first, then process the current node

---

## Binary Search Tree (BST)

A binary search tree is a special kind of binary tree with an ordering rule:

- all values in the left subtree are smaller than the current node
- all values in the right subtree are larger than the current node

This rule applies to the **entire** left subtree and the **entire** right
subtree, not only to the direct children.

Example:

```text
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

### Why BST Matters

The ordering rule allows search to be more efficient than in a general binary
tree.

At each node:

- if `target < current`, go left
- if `target > current`, go right
- if equal, the target is found

This means BST search can narrow the search space step by step instead of
blindly exploring both sides.

### Inorder Traversal in BST

In a BST, inorder traversal produces values in sorted order because:

- the left subtree contains smaller values
- the current node is in the middle
- the right subtree contains larger values

So:

```text
inorder = sorted order (for a BST)
```

### Balanced vs Skewed BST

BST efficiency depends not only on the ordering rule, but also on shape.

- A balanced BST can support efficient search
- A skewed BST can degenerate into something close to a linked list

---

## BST Search

BST search follows the ordering rule:

- if the target is smaller, go left
- if the target is larger, go right
- if the target matches the current node, return it
- if we reach `None`, the target does not exist

This is the main advantage of BST over a general binary tree.

---

## BST Insert

BST insert follows almost the same path as BST search.

To insert a value:

- start from the root
- compare the value with the current node
- go left if the value is smaller
- go right if the value is larger
- stop when the correct `None` position is found
- insert the new node there

So the idea is:

- **search** looks for whether a value exists
- **insert** looks for where a value should be placed

In recursive form, insert is naturally a subtree problem:

- insert into the left subtree, or
- insert into the right subtree

and return the updated subtree root.

---

## BST Delete

BST delete is more complex than search and insert because it must remove the
node while keeping the BST ordering rule valid.

There are three main cases.

### Case 1: Delete a Leaf

If the node has no children, remove it directly.

### Case 2: Delete a Node with One Child

If the node has exactly one child, let that child take its place.

In other words:

- if there is no left child, return the right child
- if there is no right child, return the left child

### Case 3: Delete a Node with Two Children

This is the most important BST delete case.

We usually:

1. find the inorder successor
2. replace the current node's value with the successor's value
3. delete the original successor node from the right subtree

The inorder successor is:

- the smallest value greater than the current node
- the minimum value in the right subtree
- the leftmost node in the right subtree

Why this works:

- the successor is the next valid value larger than the current node
- it can safely replace the deleted node's value
- deleting the successor from its original location is easier because it cannot
  have a left child

Short summary:

- `0 child`: remove it
- `1 child`: promote the child
- `2 children`: replace with successor, then delete successor
