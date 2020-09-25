def two_sum(nums, target):
    nums_dict = dict()
    for i, value in enumerate(nums):
        if nums_dict.get(target - value) is not None:
            return [nums_dict[target - value], i]
        nums_dict[value] = i
