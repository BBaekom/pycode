import numpy as np
import cv2 as cv

filename = 'mydata.json'
# filename = 'mydata.xml'
# filename = 'mydata.yml'

def writeData():
    name = 'Jane'
    age = 10
    pt1 = (100, 200)
    scores = (80, 90, 50)
    mat1 = np.array([[1.0, 1.5], [2.0, 3.2]], dtype=np.float32)

    fs = cv.FileStorage(filename, cv.FILE_STORAGE_WRITE)

    if not fs.isOpened():
        print('File open failed!')
        return

    fs.write('name', name)
    fs.write('age', age)
    fs.write('point', pt1)
    fs.write('scores', scores)
    fs.write('data', mat1)

    fs.release()


def readData():
    fs = cv.FileStorage(filename, cv.FILE_STORAGE_READ)

    if not fs.isOpened():
        print('File open failed!')
        return

    name = fs.getNode('name').string()
    age = int(fs.getNode('age').real())
    pt1 = tuple(fs.getNode('point').mat().astype(np.int32).flatten().tolist())
    scores = tuple(fs.getNode('scores').mat().flatten().tolist())
    # 튜플 값으로 나올 때 tolist()를 붙여야 함. --> 왜???
    mat1 = fs.getNode('data').mat()

    fs.release()

    print('name:', name)
    print('age:', age)
    print('point:', pt1)
    print('scores:', scores)
    print('data:')
    print(mat1)


# writeData()
readData()