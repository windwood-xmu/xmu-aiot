import cv2

if __name__ == '__main__':
    image = cv2.imread('1.jpg')

    blur_red = cv2.GaussianBlur(image, (11, 11), 0)

    cv2.imwrite('blur_red.jpg', blur_red)

    cv2.imshow('blue red', blur_red)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
