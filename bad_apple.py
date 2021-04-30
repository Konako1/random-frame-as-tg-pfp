import cv2
import random


def get_bad_apple_frame():
    cap = cv2.VideoCapture('bad apple.mp4')

    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    random_frame = random.randint(0, video_length)

    print(f'Frame: {random_frame}/{video_length}')

    cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame)

    while cap.isOpened():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('image\\pic.jpg', gray)
        print('done!\n')
        break
