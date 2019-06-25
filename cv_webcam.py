# -*- coding: utf-8 -*-
#!python3.6.6
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)


while True:
    ret_val, img = cap.read()
    
    # mat 文字列 座標 フォント 文字サイズ 色(b, g, r) 太さ 連結
    cv2.putText(img, 'hogehoge', (0, 50), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 1, cv2.LINE_AA)

    cv2.imshow('webcam', img)
    key = cv2.waitKey(1) & 0xff
    if key == 27:
        break  # esc to quit
    elif key == ord(' '):
        cv2.imwrite('webcam.jpg', img)
    elif ord('0') < key and key < ord('9'):
        print(key)

cv2.destroyAllWindows()