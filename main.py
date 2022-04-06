import TextDetection as td
import BalanceDegree as bd
import cv2 as cv

def main():
    filename = '02.jpeg'
    src = cv.imread(filename)

    while cv.waitKey(1) != ord('0'):
        cv.imshow("Rotated", src)

    degree = bd.find_degree(src)
    if type(degree) == str: 
        print(degree)   
        return 0

    img = bd.rotate(src, degree)
    td.test_single_img(img)
    return 1


if __name__ == '__main__' :
    print(main())
