class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,4,1]))