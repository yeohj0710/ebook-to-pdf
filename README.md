### ebook-to-pdf

- eBook을 PDF로 변환하는 프로그램
- eBook 프로그램이 노트북을 지원하지 않는 경우
  - 블루스택에서 안드로이드 에뮬레이터를 설치하여, 노트북에서 앱 실행
  - https://www.bluestacks.com/
- print_mouse_position.py
  - 마우스 포인터의 위치를 주기적으로 출력해 주는 프로그램
  - eBook에서 페이지 좌측상단과 우측하단 좌표, 다음 페이지로 넘어가는 버튼의 좌표 구하기
- ebook_to_images.py
  - 코드에서 좌표 설정 후 프로그램 실행
  - 화면 세팅 후 's'키를 눌러 자동 캡쳐 + 자동 다음 페이지 작업 수행
  - 모든 페이지 캡쳐가 끝날 때까지 기다린 후 프로그램 종료
- images_to_pdf.py
  - 불필요하게 더 캡쳐된 이미지를 삭제 후 실행
  - 자동으로 /images 폴더의 이미지 취합 후 PDF 추출됨
- OCR 작업
  - PDF24에서 무료 OCR 기능 지원
  - https://tools.pdf24.org/ko/ocr-pdf
