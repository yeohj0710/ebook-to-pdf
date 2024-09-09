from PIL import Image
import os


def convert_images_to_pdf(image_folder, output_pdf, page_size=(2480, 3508)):
    image_files = [f for f in os.listdir(image_folder) if f.endswith(".png")]
    image_files.sort(key=lambda x: int(x.split(".")[0]))

    images = []
    image_count = 0

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = Image.open(image_path)

        if img.mode == "RGBA":
            img = img.convert("RGB")

        img_ratio = img.width / img.height
        page_ratio = page_size[0] / page_size[1]

        if img_ratio > page_ratio:
            new_height = page_size[1]
            new_width = int(new_height * img_ratio)
            img = img.resize((new_width, new_height), Image.LANCZOS)
            left = (new_width - page_size[0]) // 2
            img = img.crop((left, 0, left + page_size[0], page_size[1]))
        else:
            new_width = page_size[0]
            new_height = int(new_width / img_ratio)
            img = img.resize((new_width, new_height), Image.LANCZOS)
            top = (new_height - page_size[1]) // 2
            img = img.crop((0, top, page_size[0], top + page_size[1]))

        images.append(img)
        image_count += 1

        if image_count % 10 == 0 or image_count == len(image_files):
            print(f"취합된 페이지 수: {image_count}/{len(image_files)}")

    if images:
        print("PDF 파일 저장 중...")
        images[0].save(
            output_pdf,
            save_all=True,
            append_images=images[1:],
            quality=100,
            dpi=(600, 600),
        )
        print(f"PDF 파일로 변환 완료: {output_pdf}")


image_folder = "./images"
output_pdf = "PDF.pdf"

convert_images_to_pdf(image_folder, output_pdf)
