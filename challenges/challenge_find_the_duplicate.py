def find_duplicate(nums):
    """
    >>> find_duplicate([1, 3, 4, 2, 2])
    2
    >>> find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8])
    7

    :param num:
    :return:
    """
    for num in nums:
        if type(num) != int or num < 0:
            return False
        if nums.count(num) > 1:
            return num
    return False
