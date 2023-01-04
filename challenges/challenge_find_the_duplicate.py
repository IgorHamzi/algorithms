def find_duplicate(nums):

    if len(nums) <= 1:
        return False

    nums.sort()

    j = 0

    for i in nums:
        if type(i) != int or i < 0:
            return False
        elif i != j:
            j = i
        else:
            return i

    return False
