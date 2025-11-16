class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answer[i] = product of all numbers to left of i * product of all numbers to right of i
        # make two passes through nums to build 2 arrays: left[i] stores nums[0] * ... * nums[i-1] (product of all elements to the left of i)
        # right[i] stores nums[i + 1] * ... * nums[n - 1] (product of all elements to the right of i)

        # O(1) space improvement: use answer[] as left[], use a variable R to replace the right array

        n = len(nums)
        ans = [0] * n

        ans[0] = 1 # there are no eleents to the left of first element
        for i in range(1, n): # from second element to last
            ans[i] = ans[i - 1] * nums[i - 1]
        
        R = 1
        for i in range(n - 2, -1, -1):
            R *= nums[i + 1]
            ans[i] *= R
        
        return ans 
