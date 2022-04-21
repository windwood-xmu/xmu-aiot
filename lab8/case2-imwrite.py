import cv2
from datetime import datetime

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    filename = '%s.jpg' % datetime.now().isoformat()

    cv2.imwrite(filename, frame)

    cap.release()
    cv2.destroyAllWindows()
