import pyautogui
import time


def print_mouse_position():
    try:
        while True:
            x, y = pyautogui.position()
            print(f"현재 마우스 좌표: x={x}, y={y}")
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("프로그램 중지")


if __name__ == "__main__":
    print_mouse_position()
