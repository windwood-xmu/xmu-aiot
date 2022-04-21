import cv2

if __name__ == '__main__':
    image = cv2.imread('1.jpg')

    output = image.copy()
    cv2.rectangle(
        output,
        pt1=(200, 50),
        pt2=(300, 100),
        color=(0, 0, 255),
        thickness=2
    )

    cv2.imwrite('output.jpg', output)

    cv2.destroyAllWindows()
