# -*- coding: utf-8 -*-

import cv2
import datetime

# カメラ用の設定
w, h = 400, 300
w2, h2 = w / 2, h /2
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

modeCountDown = False
start_time = 0 # タイマーの開始時刻
CountDownTime = 3 # タイマーの時間

while True:
    ret_val, img = cap.read()
    
    if modeCountDown:
        elapsed_time = (datetime.datetime.now() - start_time).total_seconds() # 経過時間
        if elapsed_time < CountDownTime: # 経過時間が設定時間より短ければ残り時間を表示する
            disp_time = CountDownTime - int(elapsed_time)
            text_str = str(disp_time)
            # mat 文字列 座標 フォント 文字サイズ 色(b, g, r) 太さ 連結
            cv2.putText(img, text_str, (w2, h2), cv2.FONT_HERSHEY_PLAIN, 10, (0, 0, 255), 5, cv2.LINE_AA)
        else: # 経過時間が設定時間を超えた段階でタイマーモード終了
            modeCountDown = False
            cv2.rectangle(img, (0, 0), (w * 2, h * 2), (255, 255, 255), -1) # 1フレームだけ白画面にする
            print('end timer: ' + str(modeCountDown))

    cv2.imshow('webcam', img)

    key = cv2.waitKey(1) & 0xff
    if key == 27 or key == ord('q'): # esc か q でプログラム終了
        break
    elif key == ord(' ') and modeCountDown == False: # spaceキーでタイマー開始
        modeCountDown = True # タイマーフラグをon
        start_time = datetime.datetime.now() # タイマーのスタート時間を保存
        print('start timer: ' + str(modeCountDown))

cv2.destroyAllWindows()