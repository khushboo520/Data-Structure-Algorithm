class Solution:
    def removeDuplicates(self, nums) -> int:
        first = 0
        second = 1
        while second < len(nums):
            if nums[first] == nums[second]:
                nums.pop(first)
            else:
                first=second
                second+=1
        print(nums)
        return len(nums)

s=Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4 ,4]))