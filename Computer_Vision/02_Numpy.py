import numpy as np


arr = ['3.14', 2., 5, 3]
n_arr = np.array(arr)
print(arr)
print(type(arr))
print(n_arr)
print(type(n_arr))

# arr = [[1, 4, 2], [7, 5, 3]]
# nums = np.array(3)
# n_arr = np.array(arr)
# np.set_printoptions(formatter={'float_kind': lambda x: "{0:0.3f}".format(x)})

# print(arr)
# print(type(arr))
# print(n_arr)
# print(type(n_arr))

# print(arr)
# print(nums)
# print(nums.ndim)
# print(nums.shape)
# print(len(nums.shape))
# print(nums.size)

# print(nums[::3])

# print(nums[1, 1])
# print(nums[1, 0:2])
# print(nums[:, 2:])
# print(nums[:, 0:2])

# print(np.zeros((2,2)))
# print(np.ones((1,2)))
# print(np.full((2,2), 7))

# print(np.random.random((2,2)))
# print(np.random.normal(loc=2, scale=2, size=(2,2)))
# print(np.random.randint(1, 10, (2,2)))


# sap = np.array([
#     "MMM", "ABT", "ABBV", "ACN", 
#     "ACE", "ATVI", "ADBE", "ADT"
# ])

# sap2d = sap.reshape(2, 4)
# print(sap2d)
# print(sap2d.T)
# print(sap2d.swapaxes(1, 0))

# grid = np.arange(16).reshape((4,4))
# # upper, lower = np.split(grid, [2])
# # print(upper)
# # print(lower)

# # 배열을 세로로 2개로 분할 (axis=1로 지정하여 열 기준 분할)
# split_grid = np.hsplit(grid, 2)

# # 각 분할된 배열 출력
# for part in split_grid:
#     print(part)

# arr1 = [100, 80, 70, 90, 110]

# celsius1 = [(f - 32) * 5 // 9 for f in arr1]

# print(celsius1)

# # 화씨 온도 배열
# arr = np.array([100, 80, 70, 90, 110])

# # 섭씨로 변환
# celsius = (arr - 32) * 5 // 9

# # 결과 출력
# print(celsius)

# a = np.arange(4) # [0, 1, 2, 3]
# b = np.arange(1, 5) # [1, 2, 3, 4]
# print(a + b) # [1, 3, 5, 7]


# # 1차원 배열
# a = np.array([1, 2, 3])

# # 2차원 배열
# b = np.array([[10, 20, 30], [40, 50, 60]])

# # 브로드캐스팅 규칙에 의해 배열 'a'의 차원이 자동으로 확장됨
# result = a + b

# print(result)