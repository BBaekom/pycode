import numpy as np

nums = np.array([[[1, 4, 2], [5, 6, 4]], [[7, 5, 3], [8, 2, 9]]])
nums = nums.reshape((3, 4))
arr1 = np.eye(3) + 2 * np.ones((3,)) + np.arange(3)
arr2 = np.vstack([nums[:, 1:2].T[0], arr1, nums[1:2, :3][0]]) * 2

print(arr1)
print(arr2)

print(np.mean(arr2, axis=0))
print(np.all(arr2 >= 8, axis=1))