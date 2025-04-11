import numpy as np


def practice_numpy():
    arr1 = np.array([7, 2, 4, 1, 3])
    arr2 = np.array([
        [1, 2, 3],
        [33, 4, 5],
        [66, 17, 8]
    ])
    # print(np.zeros((2, 2), dtype=np.int64))
    # print(np.ones((2, 3), dtype=int))
    # print(np.empty((3, 3), dtype=int))
    # print(np.arange(2, 9, 1))
    # print(np.linspace(2, 10, num=8))
    # print(np.linspace(2, 3, num=2, dtype=np.float64))

    # print(np.sort(arr1))
    # print(np.sort(arr2))
    # print(np.sort(arr2, axis=1))

    # print(np.argsort(arr2))
    # print(np.lexsort(arr2))

    # a = np.array([1,2,3])
    # b = np.array([4,5,6])
    # c = np.concatenate((a,b), axis=0)
    # print(c)

    # a = np.array([[1, 2, 3], [11, 22, 33]])
    # b = np.array([[4, 5, 6], [44, 55, 66]])
    # c = np.concatenate((a, b), axis=2)
    # print(c)

    # print(np.full((2, 3), fill_value=3, dtype=int))

    # print(np.reshape(arr2, (9,1)))

    # res = arr1[:, np.newaxis]
    # print(np.shape(res))

    # res = np.expand_dims(arr1, axis=0)
    # print(np.shape(res))
    # res = np.expand_dims(arr1, axis=1)
    # print(np.shape(res))

    # arr3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    # print(arr3[arr3 < 4])
    # print(arr3[(arr3 % 2 == 0) and (arr3 > 8)])

    # print(arr3 >= 5)
    # print(arr3[arr3 >= 5])

    # x = np.array([
    #     [1, 2],
    #     [1, 2],
    # ])
    # y = np.array([
    #     [5, 6],
    #     [5, 6],
    # ])
    # print(np.hstack((x, y)))
    # print(np.vstack((x, y)))

    # arr4 = np.arange(0, 10)
    # print(np.hsplit(arr4, (3,6)))
    # arr4 = np.arange(0, 24).reshape(6,4)
    # print(arr4)

    # arr4 = np.arange(0, 12).reshape(3, 4)
    # print(arr4)
    # res = arr4[0]
    # print(res)
    # print(type(res))
    # res[0] = 111
    # print(arr4)
    # print(res)

    # arr5 = np.arange(1, 11)
    # print(arr5)
    # res = arr5.copy()
    # print(res)

    x = np.array([
        [1, 2],
        [3, 4]
    ])
    y = np.array([
        [1, 2],
        [3, 4]
    ])
    # print(x + y)
    # print(x - y)
    # print(x * y)
    # print(x / y)

    # print(x * 10)

    # print(x.sum(axis=1))
    # print(x.max())
    # print(x.min())

    # arr6 = np.arange(1,13).reshape(3,4)
    # print(arr6)
    # print(arr6[0,1])
    # print(arr6[2:, 2])

    # rng = np.random.default_rng()
    # print(rng.random(3))
    # print(rng.integers(123, size=(2,5)))

    # rng = np.random.default_rng()
    # # print(rng.random(12))
    # res = rng.integers(123, size=(4,5))
    # print(res)
    # print(np.unique(res, return_counts=True))

    # data = np.arange(1, 13).reshape(3, 4)
    # print(data)
    # print(data.transpose())

    # data = np.arange(1, 11)[np.newaxis, :]
    # print(data.shape)
    # print(data)
    # print(np.flip(data))

    # data = np.arange(1, 13).reshape(3, 4)
    # print(data)
    # print()
    # print(np.flip(data[2]))

    # print(np.random.rand(2,3))

    data = np.arange(1, 13).reshape(3, 4)
    print(data)
    print()
    print(data[2, 1:3])

