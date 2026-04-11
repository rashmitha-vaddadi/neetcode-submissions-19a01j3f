class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

    # Pass 1: store LAST occurrence of every number
        for i, num in enumerate(numbers):
            seen[num] = i + 1  # overwrite → always keeps rightmost index

    # Pass 2: find the complement pair
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen and seen[complement] != i + 1:
                return [i + 1, seen[complement]]

        return []
        