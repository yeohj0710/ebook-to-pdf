from PyPDF2 import PdfReader, PdfWriter

input_pdf = "input.pdf"
output_pdf = "output.pdf"

# 회전할 페이지들
pages_to_rotate = [48]

# 1: 90도, 2: 180도, -1: -90도 회전
rotation_angles = [2]


reader = PdfReader(input_pdf)
writer = PdfWriter()


for i, page in enumerate(reader.pages):
    if (i + 1) in pages_to_rotate:
        idx = pages_to_rotate.index(i + 1)
        angle = rotation_angles[idx]

        rotate_degree = angle * 90
        page.rotate(rotate_degree)

    writer.add_page(page)


with open(output_pdf, "wb") as f:
    writer.write(f)

print(f"'{output_pdf}'로 저장 완료!")
