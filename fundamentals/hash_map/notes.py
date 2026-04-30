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