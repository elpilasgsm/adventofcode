import numpy

TARGET = 2020

resp = open("input.txt").readlines()

nums = numpy.unique(numpy.sort(numpy.array([int(i) for i in resp])))

for i in range(len(nums)):
    curNum = 2020 - nums[i] #2004
    for j in range(i + 1, len(nums)):
        result = numpy.where(nums == curNum - nums[j])
        if len(result[0]) > 0:
            index = result[0][0]
            number = nums[index]
            print("{} + {} + {} = {}".format(nums[i], nums[j], number, nums[i] + nums[j] + number))
            print("{} X {} X {} = {}".format(nums[i], nums[j], number, nums[i] * nums[j] * number))
