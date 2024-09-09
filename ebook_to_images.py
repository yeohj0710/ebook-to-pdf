import pyautogui
import time
from PIL import Image
import keyboard
import os


def capture_and_save_image(region, page_number):
    x1, y1, x2, y2 = region
    width = x2 - x1
    height = y2 - y1

    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
    screenshot = screenshot.resize((width * 2, height * 2))

    current_directory = os.path.dirname(os.path.abspath(__file__))
    images_directory = os.path.join(current_directory, "images")

    if not os.path.exists(images_directory):
        os.makedirs(images_directory)

    filename = os.path.join(images_directory, f"{page_number}.png")
    screenshot.save(filename, dpi=(600, 600))

    print(f"{filename}이 저장되었습니다.")


def click_button(button_coords):
    pyautogui.moveTo(button_coords[0], button_coords[1])
    pyautogui.click()


def main():
    page_number = 1
    region_to_capture = (15, 300, 1061, 1649)
    button_coords = (1024, 1692)
    capturing = False

    while True:
        if keyboard.is_pressed("s") and not capturing:
            capturing = True
            print("이미지 저장 작업을 시작합니다.")

        if capturing:
            capture_and_save_image(region_to_capture, page_number)
            click_button(button_coords)
            page_number += 1
            time.sleep(2)


if __name__ == "__main__":
    main()
