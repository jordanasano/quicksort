def quicksort(nums):
    """ Takes array of numbers.
        Returns sorted array of numbers.
    """

    if len(nums) <= 1:
        return nums

    pivot = nums.pop()

    lesser = [num for num in nums if num <= pivot]
    greater = [num for num in nums if num > pivot]

    return quicksort(lesser) + [pivot] + quicksort(greater)

print(quicksort([10,2,5,6,9,-1,-10,0]))
