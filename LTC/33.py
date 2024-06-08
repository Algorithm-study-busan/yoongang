class Solution:
    def binary_search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        if nums[0] < nums[-1]:
            return self.binary_search(nums, target)
        
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[start] <= nums[mid]:
                if nums[start] <= target and nums[mid] > target:
                    result = self.binary_search(nums[start : mid], target)
                    return  -1 if result == -1 else result + start
                else:
                    start = mid + 1
            else:
                if nums[mid] < target and nums[end] >= target:
                    result = self.binary_search(nums[mid + 1 : end + 1], target)
                    return  -1 if result == -1 else result + mid + 1
                else:
                    end = mid - 1
        return  -1
