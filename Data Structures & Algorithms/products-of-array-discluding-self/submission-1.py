class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        to_ret = []
        lefts = []
        left_cum = 1
        for n in nums:
            left_cum *= n
            lefts.append(left_cum)
        rights = []
        right_cum = 1
        for n in nums[::-1]:
            right_cum *= n
            rights.append(right_cum)
        rights = rights[::-1]
        for i in range(len(nums)):
            l = 1
            if i > 0:
                l *= lefts[i-1]
            r = 1
            if i < (len(nums) - 1):
                r *= rights[i+1]
            to_ret.append(l*r)
        return to_ret