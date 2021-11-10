## Pillow 라이브러리로 이미지 썸네일 처리하기
# pip install pillow

from PIL import Image

# PIL : Python imaging library

im = Image.open("static/dog.jpg")
im.thumbnail((800, 600))
im.save("static/dog.jpg")

im1 = Image.open("static/dog1.jpg")
im1.thumbnail((800, 600))
im1.save("static/dog1.jpg")


"""
## image Formats

- jpg / jpeg : 손실 압축( 원본 훼손 => 대신 용량이 줄어듦 ), 
                손실률(100%~0%) 손실률이 크면 클수록 이미지 용량이 줄어들음

- gif
- png
- BMP : 비트맵 
- *.ai : 일러스트 

"""
