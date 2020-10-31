import cv2
cap = cv2.VideoCapture(0)
while True:
    # 1フレームずつ取得する。
    ret, frame = cap.read()
    # フレームが取得できなかった場合は、画面を閉じる
    if not ret:
        break

    # ウィンドウに出力
    cv2.imshow("CameraApp", frame)
    key = cv2.waitKey(1)
    # Escキーを入力されたら画面を閉じる
    if key == 27 or key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
