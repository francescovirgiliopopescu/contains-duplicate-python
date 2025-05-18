from typing import List

class Solution:
  def containsDuplication(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))

sol = Solution()

nums = [1,2,3,1]

print(sol.containsDuplication(nums))