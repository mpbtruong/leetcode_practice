from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] + nums[i]== target:
                    pass


if __name__ == "__main__":
    test1 = [2,7,11,15]
    target = 9
    sol = Solution()
    print(sol.twoSum(test1, target))