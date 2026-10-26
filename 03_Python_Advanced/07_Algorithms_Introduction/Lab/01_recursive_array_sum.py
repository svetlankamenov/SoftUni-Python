def recursive_sum(nums:list, i):
    if i == len(nums) - 1:
        return nums[i]

    return nums[i] + recursive_sum(nums, i + 1)

numbers = list(map(int, input().split()))
print(recursive_sum(numbers, 0))