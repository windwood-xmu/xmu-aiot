import cv2

if __name__ == '__main__':
    image = cv2.imread('1.jpg')

    # 转为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
    cv2.imwrite('gray.jpg', gray)

    # 自己去调节 thresh 和 maxval 的参数值
    # 看看会有什么不一样的结果，从而理解参数
    retval, thresh = cv2.threshold(
        gray,
        thresh=0,
        maxval=128,
        type=cv2.THRESH_BINARY_INV
    )

    cv2.imwrite('thresh.jpg', thresh)

    cv2.destroyAllWindows()
