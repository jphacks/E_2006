import cv2
import pasteImage

cap = cv2.VideoCapture(0)
while True:
    # 1フレームずつ取得する。
    ret, frame = cap.read()
    # フレームが取得できなかった場合は、画面を閉じる
    if not ret:
        break

    # カメラに貼り付ける写真の設定周り
    img = cv2.imread('assets/sampleImage.png')
    x = -60
    y = 70
    angle = 20
    scale = 0.7
    imgpaste = pasteImage.cvpaste(img, frame, x, y, angle, scale)

    cv2.imshow('CameraApp', imgpaste)
    key = cv2.waitKey(1)

    # 終了処理
    if key == 27 or key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
