import os
import cv2

DIR_DATA = './data'

if not os.path.exists(DIR_DATA):
    os.makedirs(DIR_DATA)

no_of_classes = 24
dataset_size = 100

cap = cv2.VideoCapture(0)

for i in range(no_of_classes):
    if not os.path.exists(os.path.join(DIR_DATA, str(i))):
        os.makedirs(os.path.join(DIR_DATA, str(i)))

    print('Collecting data for class {}'.format(i))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Press Q when ready', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DIR_DATA, str(i), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()