"""
打开一个窗口，显示摄像头的内容
键盘输入 q 后，窗口退出
"""

import cv2

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow("Window Title", frame)
        keypress = cv2.waitKey(1)
        if keypress & 0x00FF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
