import pyautogui
import time
from PIL import Image
import keyboard
import os


def get_next_page_number(images_directory):
    existing_files = os.listdir(images_directory)
    png_files = sorted(
        [int(f.split(".")[0]) for f in existing_files if f.endswith(".png")]
    )

    if not png_files:
        return 1

    for i in range(1, max(png_files) + 2):
        if i not in png_files:
            return i


def capture_and_save_image(region, page_number, images_directory):
    x1, y1, x2, y2 = region
    width = x2 - x1
    height = y2 - y1

    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
    screenshot = screenshot.resize((width * 2, height * 2))

    filename = os.path.join(images_directory, f"{page_number}.png")
    screenshot.save(filename, dpi=(600, 600))

    print(f"{filename}이 저장되었습니다.")


def click_screen(screen_coords):
    pyautogui.moveTo(screen_coords[0], screen_coords[1])
    pyautogui.click()


def main():
    region_to_capture = (0, 255, 1079, 1664)
    button_coords = (1024, 1692)
    capturing = False

    current_directory = os.path.dirname(os.path.abspath(__file__))
    images_directory = os.path.join(current_directory, "images")

    if not os.path.exists(images_directory):
        os.makedirs(images_directory)

    page_number = get_next_page_number(images_directory)

    while True:
        if keyboard.is_pressed("s") and not capturing:
            capturing = True
            print("이미지 저장 작업을 시작합니다.")

        if capturing:
            keyboard.press_and_release("alt+tab")
            time.sleep(1)

            keyboard.press_and_release("alt+tab")
            time.sleep(1)

            capture_and_save_image(region_to_capture, page_number, images_directory)
            keyboard.press_and_release("right")

            page_number += 1
            time.sleep(1)


if __name__ == "__main__":
    main()
