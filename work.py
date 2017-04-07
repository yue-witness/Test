# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter
im = Image.open('test.png')
print(im.format, im.size, im.mode)

w, h = im.size
im.thumbnail((w//2, h//2))
print((w//2, h//2))

im2 = im.filter(ImageFilter.BLUR)
im2.save('1.png', 'png')
