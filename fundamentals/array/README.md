# Array
## 1. Concept
An array is a **linear** data structure that stores elements in **contiguous memory** locations and allows **direct access using indices**.

### Time Complexity

Because elements in an array are stored in **contiguous memory**, once the index is known, the position of an element can be calculated directly. Therefore, accessing an element has a time complexity of **O(1)**.

When insertion or deletion occurs, elements need to be shifted to maintain contiguity:

- **Insertion**: elements are shifted to the right
- **Deletion**: elements are shifted to the left

In the worst case, up to **n elements** (where *n* is the length of the array) need to be moved, resulting in a time complexity of **O(n)**.

Therefore:

> Arrays are efficient for **read operations** (including random access and scanning), but are not suitable for scenarios with frequent insertions or deletions.

