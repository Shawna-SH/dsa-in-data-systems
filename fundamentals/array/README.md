# Array
An array is a **linear** data structure that stores elements in **contiguous memory** locations and allows **direct access using indices**.

## Basics

Because elements in an array are stored in **contiguous memory**, once the index is known, the position of an element can be calculated directly. Therefore, accessing an element has a time complexity of **O(1)**.

When insertion or deletion occurs, elements need to be shifted to maintain contiguity:

- **Insertion**: elements are shifted to the right
- **Deletion**: elements are shifted to the left

In the worst case, up to **n elements** (where *n* is the length of the array) need to be moved, resulting in a time complexity of **O(n)**.

Therefore:

> Arrays are efficient for **read operations** (including random access and scanning), but are not suitable for scenarios with frequent insertions or deletions.

## Common Operations

### 1. Access
Read an element by index. The position can be calculated directly due to contiguous memory.

Time Complexity: **O(1)**

```python
my_array[i]
```

### 2. Update
Modify an element by index.

Time Complexity: **O(1)**

```python
my_array[i] = x
```

### 3. Traverse / Scan
Visit every element in the array.

Time Complexity: **Θ(n)**

```python
for i in range(len(my_array)):
    ...
```

### 4. Search
#### 4.1 Find the first occurrence of x
Stop once the first match is found.

Best case: **Ω(1)** (target is at the beginning)
Worst case: **O(n)** (target at the end or not present)

#### 4.2 Find all occurrences of x
Must scan the entire array, since duplicates may exist.

Time Complexity: **Θ(n)**
```python
for i in range(len(my_array)):
    if my_array[i] == target:
        ...
```

### 5. Add Element
#### 5.1 Append
A special case of insertion at the end of the array.

Usually: **O(1)** (amortized)
Worst case: **O(n)** (when resizing is required and all elements are copied)

Explanation:
Dynamic arrays (e.g., Python lists) allocate extra space. When capacity is exceeded, a new larger array is allocated and all elements are copied.

```python
my_array.append(x)
```

#### 5.2 Insert
Insert an element at a specific position.
Worst case: **O(n)** (elements must be shifted to the right)
Best case: **Ω(1)** (inserting at the end, equivalent to append)

```python
my_array.insert(i, x)
```

### 6. Delete Element
#### 6.1 Pop (last element)
A special case of deletion from the end.

Time Complexity: **O(1)**

```python
my_array.pop()
```

#### 6.2 Delete element at other positions
Remove an element from a specific index.

Worst case: **O(n)** (elements must be shifted left)
Best case: **Ω(1)** (deleting the last element)

```python
my_array.pop(i)
```

### 7. Basic Algorithms
#### 7.1. Scan + Track Maximum ([find_max](notes.py#L1-30))

To find the maximum value in an array, we must examine every element:

- Initialize the first element as the current maximum
- Traverse the array
- Update the maximum when a larger value is found

**Time Complexity**: Θ(n)  
**Space Complexity**: Θ(1)

This pattern is **commonly used** in:
- Finding minimum/maximum
- Tracking best values
- Optimization problems

#### 7.2. Scan + Collect ([find_all_occurrences](notes.py#L32-63))

To find all occurrences of a target value in an array:

- Traverse the entire array
- Collect indices that match the target

Since duplicates may exist, the algorithm cannot stop early.

**Time Complexity**: Θ(n)  
**Space Complexity**: O(k)

#### 7.3. Two Pointers

Two pointers is a common array technique that uses two indices to traverse or modify an array efficiently.

**Why use two pointers?**

In some problems, a naive approach may:
- require extra space (e.g., creating a new array), or
- involve redundant operations (e.g., multiple passes)

Two pointers help:
- reduce space usage to **O(1)** (in-place operations)
- avoid unnecessary work by processing elements from both ends
- often achieve **Θ(n)** time with a single pass

**Example: Reverse an array ([reverse_array](notes.py#L65-95))**
Use one pointer at the beginning and one at the end. Swap the two elements and move both pointers toward the center.

- Each swap fixes two elements
- No extra array is created → **O(1)** space
- All elements are processed once → **Θ(n)** time

> Two pointers reduce unnecessary work by coordinating movement from both ends or at different speeds.

**Example: Palindrome Check ([is_palindrome](notes.py#L97-127))**
Use two pointers to compare elements from both ends.

- if mismatch → return False immediately
- if all pairs match → return True