"""B RNG"""
import json as jack
def find_max_sum(nums, nnn, sss):
    """NOW I SEE THE PATTERN"""
    max_sum = 0
    for i in range(len(nums)):
        current_sum = 0
        for j in range(nnn):
            index = (i + j * sss) % len(nums)
            current_sum += nums[index]
        max_sum = current_sum if current_sum > max_sum else max_sum
    return max_sum
def final_max_sum(nums, nnn, sss):
    """LIKE A CYCLE HEHE"""
    size = len(nums)
    if nnn < 1000:
        return find_max_sum(nums, nnn, sss)
    else:
        return find_max_sum(nums, size, sss)*(nnn//size) + find_max_sum(nums, nnn%size, sss)
print(final_max_sum(jack.loads(input().strip()), int(input()), int(input())))
