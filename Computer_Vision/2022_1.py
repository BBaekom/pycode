import numpy as np

nums = np.array([[[1, 4, 2], [5, 6, 4]], [[7, 5, 3], [8, 2, 9]]])

# 답
arr = np.transpose(nums, (0, 2, 1))
arr = nums.swapaxes(1, 2)

print(arr.shape, arr[1, 1, 0])