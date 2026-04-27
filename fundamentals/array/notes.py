def find_max(arr):
    """
    Find the maximum value in an array.

    This function scans the array from left to right and keeps track of
    the current maximum value. Since every element must be checked,
    the time complexity is Θ(n).

    Args:
        arr (list): A list of comparable elements.

    Returns:
        The maximum value in the array, or None if the array is empty.

    Time Complexity:
        Θ(n)

    Space Complexity:
        Θ(1)
    """
    if not arr:
        return None

    max_value = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]

    return max_value

def find_all_occurrences(arr, target):
    """
    Find all occurrences of a target value in an array.

    This function scans the array from left to right and collects the indices
    of all occurrences of the target value. Since every element must be checked,
    the time complexity is Θ(n).

    Args:
        arr (list): A list of comparable elements.
        target: The value to search for in the array.

    Returns:
        A list of indices where the target value occurs in the array.

    Time Complexity:
        Θ(n)
    
    Space Complexity:
        O(n)
        Θ(k), where k is the number of occurrences of the target value in the array.
    """
    if not arr:
        return []
    
    occurrences = []

    for i in range(len(arr)):
        if arr[i] == target:
            occurrences.append(i)

    return occurrences

def reverse_array(arr):
    """
    Reverse an array in place using two pointers.

    This function uses one pointer at the beginning and one pointer at the end
    of the array. At each step, the two elements are swapped, and both pointers
    move toward the center.

    Args:
        arr (list): A list of elements.

    Returns:
        list: The same list after being reversed.

    Time Complexity:
        Θ(n)

    Space Complexity:
        Θ(1)
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return arr

def is_palindrome(arr):
    """
    Check whether an array is a palindrome using two pointers.

    This function compares elements from both ends of the array.
    If any pair does not match, it returns False immediately.

    Args:
        arr (list): A list of elements.

    Returns:
        bool: True if the array is a palindrome, False otherwise.

    Time Complexity:
        O(n) worst case
        Ω(1) best case

    Space Complexity:
        O(1)
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False

        left += 1
        right -= 1

    return True

def max_area(height):
    """
    Find the maximum area of water a container can store.

    Uses two pointers starting from both ends. At each step, the pointer
    with the smaller height is moved inward, since the area is limited
    by the shorter line.

    Time Complexity:
        Θ(n)

    Space Complexity:
        O(1)
    """
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        current_area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

def max_subarray_sum_k(arr, k):
    """
    Find the maximum sum of any subarray of size k.

    Uses a sliding window to avoid recomputing sums.

    Time Complexity:
        Θ(n)

    Space Complexity:
        O(1)
    """
    n = len(arr)
    if n < k:
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

def length_of_longest_substring(s):
    """
    Find the length of the longest substring without repeating characters.

    This function uses a sliding window and a set to maintain the current
    substring without duplicates. The right pointer expands the window, and
    the left pointer shrinks the window when a duplicate character appears.

    Args:
        s (str): Input string.

    Returns:
        int: Length of the longest substring without repeating characters.

    Time Complexity:
        Θ(n)

    Space Complexity:
        O(k), where k is the number of unique characters in the current window.
    """
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))     # 1
    print(length_of_longest_substring("pwwkew"))    # 3
    print(length_of_longest_substring(""))          # 0
