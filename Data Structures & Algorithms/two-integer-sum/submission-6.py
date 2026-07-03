class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HM = {}

        for i,n in enumerate(nums):
            temp = target - n
            if temp in HM:
                return [HM[temp], i]
            else:
                HM[n] =i
            