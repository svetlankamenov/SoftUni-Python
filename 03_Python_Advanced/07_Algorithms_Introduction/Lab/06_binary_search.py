def binary_search(nums: list, target: int):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    return -1

numbers = list(map(int, input().split()))
target_num = int(input())

print(binary_search(numbers, target_num))