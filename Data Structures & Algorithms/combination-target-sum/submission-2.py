class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        paths = []
        pth = []
        nums = sorted(nums)

        def backtrack(start, remaining):
            # state = pth
            # is solution met?
            if remaining == 0:
                paths.append(pth[:])
                return
            # loop over candidates
            for i in range(start, len(nums)):
                x = nums[i]
                # check if it is valid
                if x > remaining:
                    break
                # make : change the state to include the choice
                remaining -= x
                pth.append(x)
                # recurse
                backtrack(i, remaining)
                # undo the make
                remaining += x
                pth.pop()
            return
        
        backtrack(0, target)
        return paths