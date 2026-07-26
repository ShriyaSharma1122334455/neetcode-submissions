class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxcount = 0

        for i in s: 
            if (i-1) not in s:
                le = 1
                while (i + le) in s:
                    le +=1
                maxcount  = max(le, maxcount)
        return maxcount