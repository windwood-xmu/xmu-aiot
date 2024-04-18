import cv2

if __name__ == '__main__':
    image = cv2.imread('1.jpg')
    cv2.imshow('1.jpg', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

