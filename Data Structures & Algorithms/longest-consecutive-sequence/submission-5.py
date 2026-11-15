class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums = list(set(nums))
        nums = sorted(nums)
        longest = 1
        counter = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                counter += 1
                if counter > longest:
                    longest = counter
            else:
                counter = 1
        return longest