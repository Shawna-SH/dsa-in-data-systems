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

if __name__ == "__main__":
    array = [3, 1, 4, 1, 5, 9]
    print(find_max(array))  # Output: 9