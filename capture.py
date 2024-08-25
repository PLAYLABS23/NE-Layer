from os import mkdir
import cv2
from time import sleep as delay


FILE_NAME = "chabin"      # 저장되는 파일 이름
CAPTURE_DEVICE = 1      # 캡쳐 디바이스 번호
COUNTER_START = 64       # 카운터 시작 값
EXIT_VALUE = 128        # 최대 촬영 횟수

capture, counter, roi = None, None, None


def init():
    # 변수 초기화
    global capture, counter, roi
    counter = COUNTER_START
    
    # 캡쳐 장치 연결
    try:
        capture = cv2.VideoCapture(CAPTURE_DEVICE)
    except Exception as e:
        print(f"캡쳐 장치와 연결하던 중 오류가 발생했습니다!\n{e}")
        exit()
    
    # 디렉토리 생성
    try:
        mkdir("images")
    except Exception as e:
        print(f"디렉토리를 만들던 중 오류가 발생했습니다!\n{e}")
    

def main():
    global counter
    
    delay(3)

    while True:
        _, frame = capture.read()
        
        cv2.imshow("CaptureFlow - CaptureTool", frame)

        key = cv2.waitKey(1) & 0xFF
        
        try:
            path = f"./images/{FILE_NAME}{counter}.jpg"
            cv2.imwrite(path, frame)
            counter += 1
            print(f"이미지를 성공적으로 저장했습니다! : {path}")
        except Exception as e:
            print(f"이미지를 쓰려고했지만, 실패했습니다!\n{e}")
                
        if counter == EXIT_VALUE or key == ord('q'):
            break

        delay(0.5)

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    init()
    main()