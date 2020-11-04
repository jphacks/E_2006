import cv2
import pasteImage
import random
from VoiceClassification import predictor

# TODO: インデックスの設定
cap = cv2.VideoCapture(1)
img_flag = False
img_counter = 0
while True:
    key = cv2.waitKey(1)
    # 1フレームずつ取得する。
    ret, frame = cap.read()
    # フレームが取得できなかった場合は、画面を閉じる
    if not ret:
        break
    tmp = predictor.predict()
    if tmp == "Yes":
        img_flag = True

    # # TODO: ここにトリガーを記述
    # if key == 13:
    #     img_flag = True

    # TODO: 画像の複数枚対応
    if img_flag == True:
        # カメラに貼り付ける写真の設定周り
        # TODO: あとでランダムな位置に変更，画像の変更
        sample_img = cv2.imread('assets/sampleImage.png')
        x = random.randint(-50, 50)*10
        y = random.randint(-15, 15)*10
        angle = 0
        scale = 1
        # cvpaste(貼り付ける画像，動画になるフレーム，x座標(-500 ~ 500)，y座標，回転，拡大・縮小)
        imgpaste = pasteImage.cvpaste(sample_img, frame, x, y, angle, scale)

        cv2.imshow('CameraApp', imgpaste)

        img_counter += 1
        if img_counter == 10:
            img_flag = False
            img_counter = 0
    else:
        cv2.imshow('CameraApp', frame)

    # 終了処理
    if key == 27 or key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
