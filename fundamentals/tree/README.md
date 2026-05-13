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
