## Pillow 라이브러리로 이미지 썸네일 처리하기
# pip install pillow

from PIL import Image

im = Image.open("static/dog.jpg")
im.thumbnail((800, 600))
im.save("static/dog.jpg")

im1 = Image.open("static/dog1.jpg")
im1.thumbnail((800, 600))
im1.save("static/dog1.jpg")
