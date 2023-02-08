import sys
import cv2

# 비디오 캡처 초기화
cap = cv2.VideoCapture(0)
# 비디오 캡처 열렸는지 확인, 아니면 프로그램 종료
if not cap.isOpened():
    sys.exit()

# 저장한 프레임 번호 (카운터 초기화)
index = 0

# 비디오 프레임을 캡처용 루프
while True:
    # 프레임 캡처
    ret, frame = cap.read()
    # 캡처 여부 확인, 안 됐으면 종료
    if not ret:
        break
    
    # 이미지 뒤집기
    frame = cv2.flip(frame, 1)
    # frame2 = cv2.Canny(frame, 50, 150)
    
    # 텍스트용 폰트 설정
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Hello 표시
    cv2.putText(frame, 'Hello', (100,100), font,1,(255,0,0),2)
    cv2.imshow('frame', frame)
    # cv2.imshow('canny', frame2)

    key = cv2.waitKey(1)
    if key == 27: # esc 눌러 종료
        break
    # s를 눌러 이미지 저장
    elif key == ord('s'):
        # cv2.imwrite(f'my_pic_{index}.png', frame)
        cv2.imwrite(f'image/my_pic_{index}.png', frame)
        index = index + 1

cap.release()
cv2.destroyAllWindows()
