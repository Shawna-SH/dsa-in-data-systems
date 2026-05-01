# Hash map

A hash map (dictionary) is a data structure that stores key–value pairs and allows fast lookup based on keys.

Unlike an array that stores values mainly by position, a hash map stores data in an underlying bucket array. A key is passed through a hash function, and the hash value is used to calculate which bucket should store or retrieve the key–value pair.

The underlying bucket array itself is array-like, but the key–value entries are not accessed by sequential scanning. Instead, the hash map uses:

> key → hash function → bucket/index → key–value pair

If multiple keys map to the same bucket, this is called a **collision**. Collisions are handled by strategies such as chaining or open addressing, so the hash map can still find the target key.

Example:

```python
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Cathy": 78
}
```

---

## Basics

A hash map uses a **hash function** to map keys to indices in an underlying array.

This enables:

- Fast lookup by key
- Fast insertion
- Fast deletion

In most cases:

- Access: **O(1)** (average)
- Insert: **O(1)** (average)
- Delete: **O(1)** (average)

However, in worst cases (e.g., hash collisions), operations can degrade to **O(n)**.

---

## Common Operations

### 1. Access
A hash map achieves **O(1)** average lookup by using a hash function.

**Steps:**
1. Convert key into a hash value
2. Map hash to an index in an array
3. Access the value directly

> key → hash → index → O(1) lookup

```python
value = my_dict[key]
```

### 2. Insert / Update

Add or update a key–value pair.

- If the key does not exist → insert
- If the key exists → update (overwrite)

Time Complexity: **O(1)** (average)

```python
my_dict[key] = value
```

### 3. Delete

Remove a key–value pair from the hash map.

- If the key exists → the key–value pair is removed
- If the key does not exist → a KeyError will be raised (in Python)

Time Complexity: **O(1)** (average)

This is because the hash function maps the key to the relevant bucket/index directly, so the hash map does not need to scan all key–value pairs after deletion.

```python
del my_dict[key]

# Alternatively, to avoid errors when the key may not exist:
my_dict.pop(key, None)
```

### 4. Membership Check

Check whether a **key** exists in the hash map.

Time Complexity: **O(1)** (average)

This works by hashing the key and directly locating and checking the corresponding bucket, avoiding a full scan.

```python
if key in my_dict:
    ...
```

> **Note**: This checks keys, not values.  
> To check values, use `my_dict.values()`, which requires scanning all values and takes **O(n)** time.

---

## Basic Algorithms

### 1. Complement Search ([Two Sum](https://leetcode.com/problems/two-sum/description/))

Given an array `nums` and a target value, find two indices such that:

```text
nums[i] + nums[j] = target
```

**Idea**

For each element `a`, compute its complement:

```text
b = target - a
```

Use a hash map to store previously seen values and their indices.

- If `b` already exists in the map → we found the answer
- Otherwise, store `a` in the map

**Why Hash Map?**

We need to quickly check whether the complement exists.

- Array: requires scanning → O(n)
- Hash map: membership check → O(1)

This reduces the overall complexity from O(n²) to Θ(n).

- Time Complexity: **Θ(n)**
- Space Complexity: **O(n)**

> Store values you have seen so far, so you can answer future queries in O(1).

### 2. Frequency Counting ([Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/))

Given an array `arr` and an integer `k`, return the `k` most frequent elements.

```text
arr = ["a", "a", "a", "b", "b", "c"], k = 2
→ ["a", "b"]
```

**Idea**

This problem can be solved in two steps:

1. **Count frequencies using a hash map**

```text
value → frequency
```

Example:

```python
{
    "a": 3,
    "b": 2,
    "c": 1
}
```

2. **Group elements by frequency using buckets**

We create an array where the index represents the frequency:

```python
buckets = [[], [], [], [], ...]
```

Then place elements into the corresponding bucket:

```python
buckets[3] = ["a"]
buckets[2] = ["b"]
buckets[1] = ["c"]
```

**Algorithm**

- Count frequency of each element using a hash map
- Create buckets where index = frequency
- Traverse buckets from high to low frequency
- Collect elements until k elements are found

**Why Not Sort?**

Sorting all elements by frequency would take:

```text
O(n log n)
```

Using buckets avoids sorting and reduces the complexity to linear time.

**Complexity**

- Time Complexity: **Θ(n)**
- Space Complexity: **O(n)**

Each element is processed a constant number of times, and all bucket elements are visited at most once.
