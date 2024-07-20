import mediapipe as mp
import cv2
import os
import matplotlib.pyplot as plt
from mediapipe.tasks.python import vision
import pickle

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.2,
)

DIR_DATA = './data'

data = []
labels = []

NUM_LANDMARKS = 21 
LANDMARKS_PER_HAND = 2 * NUM_LANDMARKS
n= 1

for dir_ in os.listdir(DIR_DATA):
    print(n)
    n += 1
    for img_path in os.listdir(os.path.join(DIR_DATA, dir_)):
        data_aux = []
        img = cv2.imread(os.path.join(DIR_DATA, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)

        if results.multi_hand_landmarks and len(results.multi_hand_landmarks) == 1:
            hand_landmarks = results.multi_hand_landmarks[0]
            for i in range(NUM_LANDMARKS):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.extend([x, y]) 
            
            if len(data_aux) != LANDMARKS_PER_HAND:
                data_aux += [0] * (LANDMARKS_PER_HAND - len(data_aux))
        else:
            data_aux = [0] * LANDMARKS_PER_HAND

        data.append(data_aux)
        labels.append(dir_)

file = open('data.pickle','wb')
pickle.dump({'data':data, 'labels':labels},file)
file.close()