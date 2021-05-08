import cv2
import random

cap = cv2.VideoCapture('bad apple.mp4')
video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))


def get_bad_apple_frame():
    random_frame = random.randint(0, video_length)
    print(f'Frame: {random_frame}/{video_length}')
    cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame)

    while cap.isOpened():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('image\\pic.jpg', gray)
        print('done!\n')
        return random_frame


def get_every_bad_apple_frame():
    for i in range(video_length):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('all_frames\\pic' + str(i) + '.jpg', gray)
    print('done!')
