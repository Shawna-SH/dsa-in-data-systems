def two_sum(nums, target):
    """
    Find two indices such that nums[i] + nums[j] == target.

    Uses a hash map to store previously seen numbers and their indices.

    Time Complexity:
        Θ(n)

    Space Complexity:
        O(n)
    """
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            return [num_map[complement], i]

        num_map[num] = i

    return None

def top_k_frequent(arr, k):
    """
    Return the k most frequent elements in the array.

    This function first counts the frequency of each element using a hash map,
    then uses a bucket array where the index represents frequency. Elements
    are grouped into buckets based on their frequency, and the result is built
    by traversing the buckets from highest frequency to lowest.

    Args:
        arr (list): Input list of elements.
        k (int): Number of most frequent elements to return.

    Returns:
        list: A list containing the k most frequent elements.

    Time Complexity:
        Θ(n) — Each element is processed a constant number of times.

    Space Complexity:
        O(n) — For the frequency map and bucket array.
    """
    freq_map = {}
    for item in arr:
        freq_map[item] = freq_map.get(item, 0) + 1
    
    buckets = [[] for _ in range(len(arr) + 1)]
    for item, freq in freq_map.items():
        buckets[freq].append(item)
    
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for item in buckets[i]:
            result.append(item)
            if len(result) == k:
                return result
    
    return result

def subarray_sum(nums, k):
    """
    Count the number of contiguous subarrays whose sum equals k.

    This function uses prefix sum combined with a hash map to efficiently
    track how many times each cumulative sum has appeared. For each position,
    it checks how many previous prefix sums satisfy:

        current_sum - previous_sum = k

    which can be rearranged as:

        previous_sum = current_sum - k

    If such a prefix sum has appeared before, it means there exists a subarray
    ending at the current index whose sum equals k.

    Args:
        nums (list): A list of integers.
        k (int): Target subarray sum.

    Returns:
        int: The number of contiguous subarrays whose sum equals k.

    Time Complexity:
        Θ(n) — Each element is processed once.

    Space Complexity:
        O(n) — In the worst case, all prefix sums are unique.
    """
    # Stores how many times each prefix sum has occurred
    prefix_count = {0: 1}  # Base case: prefix sum = 0 appears once

    current_sum = 0  # Running prefix sum
    count = 0        # Total number of valid subarrays

    for num in nums:
        current_sum += num

        # Compute the required previous prefix sum
        need = current_sum - k

        # If 'need' exists, it means there are subarrays ending here
        # whose sum equals k
        count += prefix_count.get(need, 0)

        # Update the count of the current prefix sum
        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

    return count
