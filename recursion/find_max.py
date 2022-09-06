'''
Finding maximum value in a list wit Recursion
Algo has Time and space complexity of O(n)
'''
def max_value(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    return max_value__(nums, 0, nums[1])
def max_value__(nums: list, index: int, current: int):
    if(index == len(nums)):
        return current
    if(nums[index] > current):
        current = nums[index]
    return max_value__(nums, index+1, current)
if __name__ == "__main__":
    print(max_value([10, 5, 40, 40.3]))
