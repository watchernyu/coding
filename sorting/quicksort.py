# quicksort, last element as pivot
import numpy as np

def partition(l, r, nums):
    ptr = l
    pivot = nums[r] # in this case we use last element as pivot (can also use other elements as pivot?)
    for i in range(l, r+1):
        # check each value in the subarray [l, r], if it is smaller equal to pivot, then switch it to the left of the subarray
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    return ptr - 1 # return the location of the pivot

def _quicksort(l, r, nums):
    if l < r:
        pi = partition(l, r, nums)
        # after above line we know the pivot is at the correct final position
        # divide the remaining problem into 2 subproblems
        _quicksort(l, pi-1, nums)
        _quicksort(pi+1, r, nums)
    return nums

def quicksort(nums):
    if len(nums) == 1:
        return nums
    return _quicksort(0, len(nums)-1, nums)


example = [4, 5, 1, 2, 3]
result = [1, 2, 3, 4, 5]
print(quicksort(example))

example = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]
result = [1, 2, 2, 4, 4, 5, 6, 6, 7, 8]
# As you can see, it works for duplicates too
print(quicksort(example))

for i in range(100):
    randarray = np.random.randint(0, 100, 20)
    gt = np.sort(randarray)
    answer = quicksort(randarray)
    if not np.array_equal(gt, answer):
        print("incorrect")
        print("ground truth:", gt)
        print("answer      :", answer)
        quit()
print("all correct")

