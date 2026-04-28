# Hash map

A hash map (dictionary) is a data structure that stores key–value pairs and allows fast lookup based on keys.

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

**Collisions** may occur when multiple keys map to the same index, but are handled using techniques like chaining or open addressing.

```python
value = my_dict[key]
```