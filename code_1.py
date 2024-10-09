from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    h = {}
    for i, num in enumerate(numbers):
        h[num] = i + 1

    for i, num in enumerate(numbers):
        desired = target - num
        if desired in h and h[desired] != i:
            return i + 1, h[desired]


def removeDuplicates(arr, n):
    # Write your code here.
    i = 0
    for j in range(1, n):
        if arr[j] != arr[i]:
            arr[i + 1] = arr[j]
            i += 1
    return i + 1


if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5]
    target = 100
    # print(twoSum(numbers=numbers, target=target))
    removeDuplicates(numbers, len(numbers))
