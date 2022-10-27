def quicksort(nums):
    """ Takes array of numbers.
        Returns sorted array of numbers.
    """

    if len(nums) <= 1:
        return nums

    pivot = nums.pop()

    lesser = []
    greater = []

    for num in nums:
        if pivot >= num:
            lesser.append(num)
        else:
            greater.append(num)

    return quicksort(lesser) + [pivot] + quicksort(greater)

print(quicksort([10,2,5,6,9,-1,-10,0]))
