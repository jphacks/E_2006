import cv2
import pasteImage
import random
# from VoiceClassification import predictor

import threading
import time

# TODO: インデックスの設定
cap = cv2.VideoCapture(0)
good_img_flag = False
bad_img_flag = False
yes_img_flag = False
no_img_flag = False
clap_img_flag = False
ok_img_flag = False
raising_hand_img_flag = False
good_img_counter = 0
bad_img_counter = 0
yes_img_counter = 0
no_img_counter = 0
clap_img_counter = 0
ok_img_counter = 0
raising_hand_img_counter = 0
img_display_time = 10

ml_flag = False

while True:
    key = cv2.waitKey(1)
    # 1フレームずつ取得する。
    ret, frame = cap.read()
    # フレームが取得できなかった場合は、画面を閉じる
    if not ret:
        break

    with open("VoiceClassification/result.txt", mode="r", errors='ignore', encoding="utf-8")as f:
        text = f.read()

    if key == ord("m"):
        ml_flag = not ml_flag

    if ml_flag:
        if text == "Yes":
            yes_img_flag = True
        if text == "No":
            no_img_flag = True
        if text == "Clap":
            clap_img_flag = True

    # 各種トリガーを記述
    if key == ord("g"):
        good_img_flag = True
    if key == ord("b"):
        bad_img_flag = True
    if key == ord("y"):
        yes_img_flag = True
    if key == ord("n"):
        no_img_flag = True
    if key == ord("c"):
        clap_img_flag = True
    if key == ord("o"):
        ok_img_flag = True
    if key == ord("h"):
        raising_hand_img_flag = True

    # 各画像の表示
    # default images
    paste_img = cv2.imread('assets/keyboard-actions.png')
    x = -500
    y = -150
    angle = 0
    scale = 0.5
    frame = pasteImage.cvpaste(paste_img, frame, x, y, angle, scale)
    # keyboard actions images
    if good_img_flag == True:
        paste_img = cv2.imread('assets/good.png')
        x = -300
        y = 200
        angle = 0
        scale = 1.2
        frame = pasteImage.cvpaste(paste_img, frame, x, y, angle, scale)
        good_img_counter += 1
        if good_img_counter == img_display_time:
            good_img_flag = False
            good_img_counter = 0
    if bad_img_flag == True:
        paste_img = cv2.imread('assets/bad.png')
        x = 300
        y = 200
        angle = 0
        scale = 1.2
        frame = pasteImage.cvpaste(paste_img, frame, x, y, angle, scale)
        bad_img_counter += 1
        if bad_img_counter == img_display_time:
            bad_img_flag = False
            bad_img_counter = 0
    if yes_img_flag == True:
        paste_img = cv2.imread('assets/yes.png')
        x = 450
        y = -120
        angle = 0
        scale = 1.5
        frame = pasteImage.cvpaste(paste_img, frame, x, y, angle, scale)
        yes_img_counter += 1
        if yes_img_counter == img_display_time:
            yes_img_flag = False
            yes_img_counter = 0
    if no_img_flag == True:
        paste_img = cv2.imread('assets/no.png')
        x = 450
        y = 120
        angle = 0
        scale = 1
        frame = pasteImage.cvpaste(paste_img, frame, x, y, angle, scale)
        no_img_counter += 1
        if no_img_counter == img_display_time:
            no_img_flag = False
            no_img_counter = 0
    if clap_img_flag == True:
        paste_img = cv2.imread('assets/clap.png')
        x = random.randint(-50, 50)*10
        y = random.randint(-15, 15)*10
        angle = 0
        scale = 1.2
        frame = pasteImage.cvpaste(paste_img, frame, x, y, angle, scale)
        clap_img_counter += 1
        if clap_img_counter == img_display_time:
            clap_img_flag = False
            clap_img_counter = 0
    if ok_img_flag == True:
        paste_img = cv2.imread('assets/ok.png')
        x = 0
        y = 0
        angle = 0
        scale = 1.2
        frame = pasteImage.cvpaste(paste_img, frame, x, y, angle, scale)
        ok_img_counter += 1
        if ok_img_counter == img_display_time:
            ok_img_flag = False
            ok_img_counter = 0
    if raising_hand_img_flag == True:
        paste_img = cv2.imread('assets/raising_hand.png')
        x = -500
        y = 200
        angle = 0
        scale = 1.2
        frame = pasteImage.cvpaste(paste_img, frame, x, y, angle, scale)
        raising_hand_img_counter += 1
        if raising_hand_img_counter == img_display_time:
            raising_hand_img_flag = False
            raising_hand_img_counter = 0

    cv2.imshow('CameraApp', frame)

    # 終了処理
    if key == 27 or key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
