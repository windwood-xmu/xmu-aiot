import cv2

if __name__ == '__main__':
    image = cv2.imread('1.jpg')

    # 转为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
    cv2.imwrite('gray.jpg', gray)

    # 边缘检测
    edged = cv2.Canny(gray, 30, 150)
    cv2.imwrite('edged.jpg', edged)

    cv2.destroyAllWindows()
