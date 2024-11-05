import os
from PyPDF2 import PdfMerger
from tqdm import tqdm

pdf_files = [
    f"{i}.pdf" for i in range(1, len(os.listdir()) + 1) if f"{i}.pdf" in os.listdir()
]
pdf_files.sort()

pdf_merger = PdfMerger()

print("PDF 파일을 병합하는 중...")
for pdf in tqdm(pdf_files, desc="병합 진행", unit="file"):
    pdf_merger.append(pdf)

output_filename = "merged_output.pdf"
pdf_merger.write(output_filename)
pdf_merger.close()
print(f"\n병합된 PDF가 '{output_filename}' 이름으로 저장되었습니다.")
