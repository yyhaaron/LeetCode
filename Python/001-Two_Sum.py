## 09/14/18 First trial

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = sorted(range(len(nums)), key=lambda k: nums[k])
        nums2 = sorted(nums)

        a = 0
        b = len(nums)-1
        search = 1
        while ((a < b) & search):
            if(nums2[a] + nums2[b] > target):
                b = b - 1
            elif(nums2[a] + nums2[b] < target):
                a = a + 1
            elif(nums2[a] + nums2[b] == target):
                search = 0
                
        return [index[a], index[b]]
 
        
        
