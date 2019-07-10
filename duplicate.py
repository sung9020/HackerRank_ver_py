class Solution:
    def removeDuplicates(self, nums):
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)

# 함수내의 객체 주소 할당이 안통하는듯... 슬라이싱으로 할당하니 되네..?