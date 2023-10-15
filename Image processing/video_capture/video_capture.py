import cv2
import datetime

video_capture = cv2.VideoCapture(0)

while (True):

    grabbed, frame = video_capture.read()
    cv2.imshow('Original Video', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        file = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f") + '.jpg'
        cv2.imwrite(file, frame)
        print(file, ' saved')

video_capture.release()
cv2.destroyAllWindows()